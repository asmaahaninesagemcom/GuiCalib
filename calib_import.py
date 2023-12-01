#! /usr/bin/env python
#  -*- coding: utf-8 -*-


def data_importation():
    """
    Génère: referentiel.csv
            tranformetemp.scv
            cal.pkl
    """
    temp = str2intArray(Temp.get())
    seqComplete = str2intArray(Seq.get())

    dfAll,df, allFiles = loadCsv()
    # Sauvegarde du dernier fichier dans une autre database pour le transformer plus tard dans un référentiel
    randomFile = df.copy()

    try:
        os.makedirs('Output')
    except OSError:
        if not os.path.isdir('Output'):
            raise

    # Compteur des observations
    dfAll['counter'] = dfAll.groupby(['Spool Piece', 'temprg', 'flowrg']).cumcount() + 1
    # Filtre sur les variables retenues
    dfAll = dfAll[
        ['Spool Piece', 'counter', 'temprg', 'factor_corr', 'AVR_TOF_SUM', 'temp', 'bflow', 'date', 'flowrg', 'dtofc']]

    # Filtre sur les temperatures a 20 deg avant de creer la table pivot
    df20 = dfAll[dfAll.temprg == 20]

    # Recuperation du facteur et tof sum a 20 uniquement par spool piece, information qu'on va ajouter plus tard
    fact_tof = df20[['Spool Piece', 'factor_corr', 'AVR_TOF_SUM', 'bflow']]
    fact_tof = fact_tof[fact_tof.bflow.round() == 3125]
    fact_tof.drop('bflow', axis=1, inplace=True)
    fact_tof['factor_corr_x_avr_tof'] = fact_tof.factor_corr * fact_tof.AVR_TOF_SUM

    # Creation du pivot autour de la database a 20 deg
    # Tous les dtofc passent aussi en colonne
    df2 = df20.pivot_table(index=['Spool Piece', 'counter'], columns='flowrg', values=['dtofc'])

    # Filtre de la database avec tous les cals, on garde que les colones pertinentes
    data = dfAll[['Spool Piece', 'counter', 'temprg', 'temp', 'bflow', 'flowrg', 'date', 'dtofc']]

    # Merge de la base pivot (a 20) avec la base originale
    data2 = df2.merge(data, on=['Spool Piece', 'counter'])
    df = data2.copy()

    # Actualisation des noms des colonnes de la database
    df.columns = ['Spool Piece', 'counter'] + ["dtofc_" + str(i) for i in seqComplete]+['temprg', 'temp', 'bflow', 'flowrg', 'date', 'dtofc']

    # Jointure avec les informations sur le facteur et le sumtof a 20
    df = df.merge(fact_tof, on='Spool Piece', how="inner")

    # Suppression de la variable counter qu'on utilise plus
    df.drop('counter', axis=1, inplace=True)
    # Sauvegarde de la base intermédiaire
    df.to_csv(r'Output\transformetemp.csv', index=False)

    # Creation d'un fichier avec 3 informations principales:
    #   le bflow (arrondi a 2 decimales)
    #   le refvol - volume d'eau utilisé pour ce flow
    #   le nom de la variable qui correspond au dtofc du debit
    randomFile['bflow'] = randomFile.bflow.round(2)
    randomFile = randomFile[['bflow', 'refvol']]
    randomFile['nomv'] = ["dtofc_" + str(i) for i in seqComplete]

    # Calcul du temps teorique necessaire pour tester ce volume, en minutes
    randomFile['temps'] = randomFile.refvol / randomFile.bflow * 60
    # Sauvegarde du fichier avec les information sur les flows
    randomFile.to_excel(r"Output\referentiel_duree.xlsx", index=False)

    # Recuperation de 3 fichiers CAL aleatoires, 1 a chaque temperature,
    # sur la base desquels nous allons creer en production les cals de sortie
    allFiles = os.listdir(ImportPath.get())

    # Lecture de ces 3 fichiers
    file_temp = []
    df_temp = []
    for i in np.arange(len(temp)):
        file_temp.append(random.choice([file for file in allFiles if str(str(int(temp[i])) + "deg") in file]))
        df_temp.append(pd.read_csv(file_temp[i], sep=";", header=0))

    liste_df = [df_temp[i] for i in np.arange(len(temp))]
    os.chdir(str(ImportPath.get() + '\Output'))
    with open('cals_type.pkl', 'wb') as handle:
        pkl.dump(liste_df, handle, protocol=pkl.HIGHEST_PROTOCOL)

    return 0
