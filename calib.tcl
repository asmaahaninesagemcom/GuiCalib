#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Aug 30, 2021 04:41:30 PM CEST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 0
set vTcl(mode) Absolute
}




proc vTclWindow.top37 {base} {
    global vTcl
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1265x770+188+68
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1265 770
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm title $top "Searcher"
    vTcl:DefineAlias "$top" "import" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra38 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 265 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 1246 
    vTcl:DefineAlias "$top.fra38" "frameImport" vTcl:WidgetProc "import" 1
    set site_3_0 $top.fra38
    label $site_3_0.lab40 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Path to search: } 
    vTcl:DefineAlias "$site_3_0.lab40" "LabelPathImp" vTcl:WidgetProc "import" 1
    entry $site_3_0.ent41 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable ImportPath 
    vTcl:DefineAlias "$site_3_0.ent41" "txtPathImport" vTcl:WidgetProc "import" 1
    vTcl:copy_lock $site_3_0.ent41
    button $site_3_0.but42 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command OnBtnSearchPath \
        -disabledforeground #a3a3a3 -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text ... 
    vTcl:DefineAlias "$site_3_0.but42" "btnSearchPath" vTcl:WidgetProc "import" 1
    button $site_3_0.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Import 
    vTcl:DefineAlias "$site_3_0.but46" "btnImport" vTcl:WidgetProc "import" 1
    bind $site_3_0.but46 <Button-1> {
        lambda e: OnBtnGo(e)
    }
    entry $site_3_0.ent45 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable Temp 
    vTcl:DefineAlias "$site_3_0.ent45" "txtTemp" vTcl:WidgetProc "import" 1
    entry $site_3_0.ent46 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable Seq 
    vTcl:DefineAlias "$site_3_0.ent46" "txtSeq" vTcl:WidgetProc "import" 1
    entry $site_3_0.ent47 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable Mes 
    vTcl:DefineAlias "$site_3_0.ent47" "txtMes" vTcl:WidgetProc "import" 1
    label $site_3_0.lab48 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text Températures 
    vTcl:DefineAlias "$site_3_0.lab48" "LabelTemp" vTcl:WidgetProc "import" 1
    label $site_3_0.lab49 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text Séquence 
    vTcl:DefineAlias "$site_3_0.lab49" "LabelSeq" vTcl:WidgetProc "import" 1
    label $site_3_0.lab50 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text {Débits Mesurés} 
    vTcl:DefineAlias "$site_3_0.lab50" "LabelMes" vTcl:WidgetProc "import" 1
    ttk::style configure Treeview \
         -font  "$vTcl(actual_gui_font_treeview_desc)"
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $site_3_0.scr52 \
        -background $vTcl(actual_gui_bg) 
    vTcl:DefineAlias "$site_3_0.scr52" "Scrolledtreeview1" vTcl:WidgetProc "import" 1
    bind $site_3_0.scr52 <Button-1> {
        lambda e: OnTreeviewClick(e)
    }

    .top37.fra38.scr52.01 configure -height 4
        .top37.fra38.scr52.01 configure -columns {}
        .top37.fra38.scr52.01 heading #0 -anchor center
        .top37.fra38.scr52.01 column #0 -width 200
        .top37.fra38.scr52.01 column #0 -minwidth 20
        .top37.fra38.scr52.01 column #0 -stretch 1
        .top37.fra38.scr52.01 column #0 -anchor w
    place $site_3_0.lab40 \
        -in $site_3_0 -x 40 -y 40 -width 90 -relwidth 0 -height 19 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent41 \
        -in $site_3_0 -x 140 -y 40 -width 396 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but42 \
        -in $site_3_0 -x 540 -y 30 -width 38 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 150 -y 200 -anchor nw -bordermode ignore 
    place $site_3_0.ent45 \
        -in $site_3_0 -x 140 -y 80 -width 396 -height 31 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent46 \
        -in $site_3_0 -x 140 -y 120 -width 396 -height 31 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent47 \
        -in $site_3_0 -x 140 -y 160 -width 396 -height 31 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 40 -y 80 -width 90 -relwidth 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 40 -y 120 -width 90 -relwidth 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 40 -y 160 -width 90 -relwidth 0 -anchor nw \
        -bordermode ignore 
    frame $top.fra39 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 265 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 761 
    vTcl:DefineAlias "$top.fra39" "frameGenerate" vTcl:WidgetProc "import" 1
    button $top.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Exit 
    vTcl:DefineAlias "$top.but51" "btnExit_1" vTcl:WidgetProc "import" 1
    bind $top.but51 <Button-1> {
        lambda e: OnBtnExit(e)
    }
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 10 -y 10 -width 1246 -relwidth 0 -height 254 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra39 \
        -in $top -x 10 -y 270 -width 1246 -relwidth 0 -height 254 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 1151 -y 709 -width 79 -height 37 -anchor nw \
        -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

