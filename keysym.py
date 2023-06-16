keysymnames = {
    "NoSymbol":                    0x000000,  # Special KeySym
    "VoidSymbol":                  0xffffff,  # Void symbol
    "BackSpace":                     0xff08,  # Back space, back char
    "Tab":                           0xff09,
    "Linefeed":                      0xff0a,  # Linefeed, LF
    "Clear":                         0xff0b,
    "Return":                        0xff0d,  # Return, enter
    "Pause":                         0xff13,  # Pause, hold
    "Scroll_Lock":                   0xff14,
    "Sys_Req":                       0xff15,
    "Escape":                        0xff1b,
    "Delete":                        0xffff,  # Delete, rubout
    "Multi_key":                     0xff20,  # Multi-key character compose
    "Codeinput":                     0xff37,
    "SingleCandidate":               0xff3c,
    "MultipleCandidate":             0xff3d,
    "PreviousCandidate":             0xff3e,
    "Kanji":                         0xff21,  # Kanji, Kanji convert
    "Muhenkan":                      0xff22,  # Cancel Conversion
    "Henkan_Mode":                   0xff23,  # Start/Stop Conversion
    "Henkan":                        0xff23,  # Alias for Henkan_Mode
    "Romaji":                        0xff24,  # to Romaji
    "Hiragana":                      0xff25,  # to Hiragana
    "Katakana":                      0xff26,  # to Katakana
    "Hiragana_Katakana":             0xff27,  # Hiragana/Katakana toggle
    "Zenkaku":                       0xff28,  # to Zenkaku
    "Hankaku":                       0xff29,  # to Hankaku
    "Zenkaku_Hankaku":               0xff2a,  # Zenkaku/Hankaku toggle
    "Touroku":                       0xff2b,  # Add to Dictionary
    "Massyo":                        0xff2c,  # Delete from Dictionary
    "Kana_Lock":                     0xff2d,  # Kana Lock
    "Kana_Shift":                    0xff2e,  # Kana Shift
    "Eisu_Shift":                    0xff2f,  # Alphanumeric Shift
    "Eisu_toggle":                   0xff30,  # Alphanumeric toggle
    "Kanji_Bangou":                  0xff37,  # Codeinput
    "Zen_Koho":                      0xff3d,  # Multiple/All Candidate(s)
    "Mae_Koho":                      0xff3e,  # Previous Candidate
    "Home":                          0xff50,
    "Left":                          0xff51,  # Move left, left arrow
    "Up":                            0xff52,  # Move up, up arrow
    "Right":                         0xff53,  # Move right, right arrow
    "Down":                          0xff54,  # Move down, down arrow
    "Prior":                         0xff55,  # Prior, previous
    "Page_Up":                       0xff55,
    "Next":                          0xff56,  # Next
    "Page_Down":                     0xff56,
    "End":                           0xff57,  # EOL
    "Begin":                         0xff58,  # BOL
    "Select":                        0xff60,  # Select, mark
    "Print":                         0xff61,
    "Execute":                       0xff62,  # Execute, run, do
    "Insert":                        0xff63,  # Insert, insert here
    "Undo":                          0xff65,
    "Redo":                          0xff66,  # Redo, again
    "Menu":                          0xff67,
    "Find":                          0xff68,  # Find, search
    "Cancel":                        0xff69,  # Cancel, stop, abort, exit
    "Help":                          0xff6a,  # Help
    "Break":                         0xff6b,
    "Mode_switch":                   0xff7e,  # Character set switch
    "script_switch":                 0xff7e,  # Alias for mode_switch
    "Num_Lock":                      0xff7f,
    "KP_Space":                      0xff80,  # Space
    "KP_Tab":                        0xff89,
    "KP_Enter":                      0xff8d,  # Enter
    "KP_F1":                         0xff91,  # PF1, KP_A, ...
    "KP_F2":                         0xff92,
    "KP_F3":                         0xff93,
    "KP_F4":                         0xff94,
    "KP_Home":                       0xff95,
    "KP_Left":                       0xff96,
    "KP_Up":                         0xff97,
    "KP_Right":                      0xff98,
    "KP_Down":                       0xff99,
    "KP_Prior":                      0xff9a,
    "KP_Page_Up":                    0xff9a,
    "KP_Next":                       0xff9b,
    "KP_Page_Down":                  0xff9b,
    "KP_End":                        0xff9c,
    "KP_Begin":                      0xff9d,
    "KP_Insert":                     0xff9e,
    "KP_Delete":                     0xff9f,
    "KP_Equal":                      0xffbd,  # Equals
    "KP_Multiply":                   0xffaa,
    "KP_Add":                        0xffab,
    "KP_Separator":                  0xffac,  # Separator, often comma
    "KP_Subtract":                   0xffad,
    "KP_Decimal":                    0xffae,
    "KP_Divide":                     0xffaf,
    "KP_0":                          0xffb0,
    "KP_1":                          0xffb1,
    "KP_2":                          0xffb2,
    "KP_3":                          0xffb3,
    "KP_4":                          0xffb4,
    "KP_5":                          0xffb5,
    "KP_6":                          0xffb6,
    "KP_7":                          0xffb7,
    "KP_8":                          0xffb8,
    "KP_9":                          0xffb9,
    "F1":                            0xffbe,
    "F2":                            0xffbf,
    "F3":                            0xffc0,
    "F4":                            0xffc1,
    "F5":                            0xffc2,
    "F6":                            0xffc3,
    "F7":                            0xffc4,
    "F8":                            0xffc5,
    "F9":                            0xffc6,
    "F10":                           0xffc7,
    "F11":                           0xffc8,
    "L1":                            0xffc8,
    "F12":                           0xffc9,
    "L2":                            0xffc9,
    "F13":                           0xffca,
    "L3":                            0xffca,
    "F14":                           0xffcb,
    "L4":                            0xffcb,
    "F15":                           0xffcc,
    "L5":                            0xffcc,
    "F16":                           0xffcd,
    "L6":                            0xffcd,
    "F17":                           0xffce,
    "L7":                            0xffce,
    "F18":                           0xffcf,
    "L8":                            0xffcf,
    "F19":                           0xffd0,
    "L9":                            0xffd0,
    "F20":                           0xffd1,
    "L10":                           0xffd1,
    "F21":                           0xffd2,
    "R1":                            0xffd2,
    "F22":                           0xffd3,
    "R2":                            0xffd3,
    "F23":                           0xffd4,
    "R3":                            0xffd4,
    "F24":                           0xffd5,
    "R4":                            0xffd5,
    "F25":                           0xffd6,
    "R5":                            0xffd6,
    "F26":                           0xffd7,
    "R6":                            0xffd7,
    "F27":                           0xffd8,
    "R7":                            0xffd8,
    "F28":                           0xffd9,
    "R8":                            0xffd9,
    "F29":                           0xffda,
    "R9":                            0xffda,
    "F30":                           0xffdb,
    "R10":                           0xffdb,
    "F31":                           0xffdc,
    "R11":                           0xffdc,
    "F32":                           0xffdd,
    "R12":                           0xffdd,
    "F33":                           0xffde,
    "R13":                           0xffde,
    "F34":                           0xffdf,
    "R14":                           0xffdf,
    "F35":                           0xffe0,
    "R15":                           0xffe0,
    "Shift_L":                       0xffe1,  # Left shift
    "Shift_R":                       0xffe2,  # Right shift
    "Control_L":                     0xffe3,  # Left control
    "Control_R":                     0xffe4,  # Right control
    "Caps_Lock":                     0xffe5,  # Caps lock
    "Shift_Lock":                    0xffe6,  # Shift lock
    "Meta_L":                        0xffe7,  # Left meta
    "Meta_R":                        0xffe8,  # Right meta
    "Alt_L":                         0xffe9,  # Left alt
    "Alt_R":                         0xffea,  # Right alt
    "Super_L":                       0xffeb,  # Left super
    "Super_R":                       0xffec,  # Right super
    "Hyper_L":                       0xffed,  # Left hyper
    "Hyper_R":                       0xffee,  # Right hyper
    "ISO_Lock":                      0xfe01,
    "ISO_Level2_Latch":              0xfe02,
    "ISO_Level3_Shift":              0xfe03,
    "ISO_Level3_Latch":              0xfe04,
    "ISO_Level3_Lock":               0xfe05,
    "ISO_Level5_Shift":              0xfe11,
    "ISO_Level5_Latch":              0xfe12,
    "ISO_Level5_Lock":               0xfe13,
    "ISO_Group_Shift":               0xff7e,  # Alias for mode_switch
    "ISO_Group_Latch":               0xfe06,
    "ISO_Group_Lock":                0xfe07,
    "ISO_Next_Group":                0xfe08,
    "ISO_Next_Group_Lock":           0xfe09,
    "ISO_Prev_Group":                0xfe0a,
    "ISO_Prev_Group_Lock":           0xfe0b,
    "ISO_First_Group":               0xfe0c,
    "ISO_First_Group_Lock":          0xfe0d,
    "ISO_Last_Group":                0xfe0e,
    "ISO_Last_Group_Lock":           0xfe0f,
    "ISO_Left_Tab":                  0xfe20,
    "ISO_Move_Line_Up":              0xfe21,
    "ISO_Move_Line_Down":            0xfe22,
    "ISO_Partial_Line_Up":           0xfe23,
    "ISO_Partial_Line_Down":         0xfe24,
    "ISO_Partial_Space_Left":        0xfe25,
    "ISO_Partial_Space_Right":       0xfe26,
    "ISO_Set_Margin_Left":           0xfe27,
    "ISO_Set_Margin_Right":          0xfe28,
    "ISO_Release_Margin_Left":       0xfe29,
    "ISO_Release_Margin_Right":      0xfe2a,
    "ISO_Release_Both_Margins":      0xfe2b,
    "ISO_Fast_Cursor_Left":          0xfe2c,
    "ISO_Fast_Cursor_Right":         0xfe2d,
    "ISO_Fast_Cursor_Up":            0xfe2e,
    "ISO_Fast_Cursor_Down":          0xfe2f,
    "ISO_Continuous_Underline":      0xfe30,
    "ISO_Discontinuous_Underline":   0xfe31,
    "ISO_Emphasize":                 0xfe32,
    "ISO_Center_Object":             0xfe33,
    "ISO_Enter":                     0xfe34,
    "dead_grave":                    0xfe50,
    "dead_acute":                    0xfe51,
    "dead_circumflex":               0xfe52,
    "dead_tilde":                    0xfe53,
    "dead_perispomeni":              0xfe53,  # alias for dead_tilde
    "dead_macron":                   0xfe54,
    "dead_breve":                    0xfe55,
    "dead_abovedot":                 0xfe56,
    "dead_diaeresis":                0xfe57,
    "dead_abovering":                0xfe58,
    "dead_doubleacute":              0xfe59,
    "dead_caron":                    0xfe5a,
    "dead_cedilla":                  0xfe5b,
    "dead_ogonek":                   0xfe5c,
    "dead_iota":                     0xfe5d,
    "dead_voiced_sound":             0xfe5e,
    "dead_semivoiced_sound":         0xfe5f,
    "dead_belowdot":                 0xfe60,
    "dead_hook":                     0xfe61,
    "dead_horn":                     0xfe62,
    "dead_stroke":                   0xfe63,
    "dead_abovecomma":               0xfe64,
    "dead_psili":                    0xfe64,  # alias for dead_abovecomma
    "dead_abovereversedcomma":       0xfe65,
    "dead_dasia":                    0xfe65,  # alias for dead_abovereversedcomma
    "dead_doublegrave":              0xfe66,
    "dead_belowring":                0xfe67,
    "dead_belowmacron":              0xfe68,
    "dead_belowcircumflex":          0xfe69,
    "dead_belowtilde":               0xfe6a,
    "dead_belowbreve":               0xfe6b,
    "dead_belowdiaeresis":           0xfe6c,
    "dead_invertedbreve":            0xfe6d,
    "dead_belowcomma":               0xfe6e,
    "dead_currency":                 0xfe6f,
    "dead_lowline":                  0xfe90,
    "dead_aboveverticalline":        0xfe91,
    "dead_belowverticalline":        0xfe92,
    "dead_longsolidusoverlay":       0xfe93,
    "dead_a":                        0xfe80,
    "dead_A":                        0xfe81,
    "dead_e":                        0xfe82,
    "dead_E":                        0xfe83,
    "dead_i":                        0xfe84,
    "dead_I":                        0xfe85,
    "dead_o":                        0xfe86,
    "dead_O":                        0xfe87,
    "dead_u":                        0xfe88,
    "dead_U":                        0xfe89,
    "dead_small_schwa":              0xfe8a,
    "dead_capital_schwa":            0xfe8b,
    "dead_greek":                    0xfe8c,
    "First_Virtual_Screen":          0xfed0,
    "Prev_Virtual_Screen":           0xfed1,
    "Next_Virtual_Screen":           0xfed2,
    "Last_Virtual_Screen":           0xfed4,
    "Terminate_Server":              0xfed5,
    "AccessX_Enable":                0xfe70,
    "AccessX_Feedback_Enable":       0xfe71,
    "RepeatKeys_Enable":             0xfe72,
    "SlowKeys_Enable":               0xfe73,
    "BounceKeys_Enable":             0xfe74,
    "StickyKeys_Enable":             0xfe75,
    "MouseKeys_Enable":              0xfe76,
    "MouseKeys_Accel_Enable":        0xfe77,
    "Overlay1_Enable":               0xfe78,
    "Overlay2_Enable":               0xfe79,
    "AudibleBell_Enable":            0xfe7a,
    "Pointer_Left":                  0xfee0,
    "Pointer_Right":                 0xfee1,
    "Pointer_Up":                    0xfee2,
    "Pointer_Down":                  0xfee3,
    "Pointer_UpLeft":                0xfee4,
    "Pointer_UpRight":               0xfee5,
    "Pointer_DownLeft":              0xfee6,
    "Pointer_DownRight":             0xfee7,
    "Pointer_Button_Dflt":           0xfee8,
    "Pointer_Button1":               0xfee9,
    "Pointer_Button2":               0xfeea,
    "Pointer_Button3":               0xfeeb,
    "Pointer_Button4":               0xfeec,
    "Pointer_Button5":               0xfeed,
    "Pointer_DblClick_Dflt":         0xfeee,
    "Pointer_DblClick1":             0xfeef,
    "Pointer_DblClick2":             0xfef0,
    "Pointer_DblClick3":             0xfef1,
    "Pointer_DblClick4":             0xfef2,
    "Pointer_DblClick5":             0xfef3,
    "Pointer_Drag_Dflt":             0xfef4,
    "Pointer_Drag1":                 0xfef5,
    "Pointer_Drag2":                 0xfef6,
    "Pointer_Drag3":                 0xfef7,
    "Pointer_Drag4":                 0xfef8,
    "Pointer_Drag5":                 0xfefd,
    "Pointer_EnableKeys":            0xfef9,
    "Pointer_Accelerate":            0xfefa,
    "Pointer_DfltBtnNext":           0xfefb,
    "Pointer_DfltBtnPrev":           0xfefc,
    "ch":                            0xfea0,
    "Ch":                            0xfea1,
    "CH":                            0xfea2,
    "c_h":                           0xfea3,
    "C_h":                           0xfea4,
    "C_H":                           0xfea5,
    "3270_Duplicate":                0xfd01,
    "3270_FieldMark":                0xfd02,
    "3270_Right2":                   0xfd03,
    "3270_Left2":                    0xfd04,
    "3270_BackTab":                  0xfd05,
    "3270_EraseEOF":                 0xfd06,
    "3270_EraseInput":               0xfd07,
    "3270_Reset":                    0xfd08,
    "3270_Quit":                     0xfd09,
    "3270_PA1":                      0xfd0a,
    "3270_PA2":                      0xfd0b,
    "3270_PA3":                      0xfd0c,
    "3270_Test":                     0xfd0d,
    "3270_Attn":                     0xfd0e,
    "3270_CursorBlink":              0xfd0f,
    "3270_AltCursor":                0xfd10,
    "3270_KeyClick":                 0xfd11,
    "3270_Jump":                     0xfd12,
    "3270_Ident":                    0xfd13,
    "3270_Rule":                     0xfd14,
    "3270_Copy":                     0xfd15,
    "3270_Play":                     0xfd16,
    "3270_Setup":                    0xfd17,
    "3270_Record":                   0xfd18,
    "3270_ChangeScreen":             0xfd19,
    "3270_DeleteWord":               0xfd1a,
    "3270_ExSelect":                 0xfd1b,
    "3270_CursorSelect":             0xfd1c,
    "3270_PrintScreen":              0xfd1d,
    "3270_Enter":                    0xfd1e,
    "space":                         0x0020,  # U+0020 SPACE
    "exclam":                        0x0021,  # U+0021 EXCLAMATION MARK
    "quotedbl":                      0x0022,  # U+0022 QUOTATION MARK
    "numbersign":                    0x0023,  # U+0023 NUMBER SIGN
    "dollar":                        0x0024,  # U+0024 DOLLAR SIGN
    "percent":                       0x0025,  # U+0025 PERCENT SIGN
    "ampersand":                     0x0026,  # U+0026 AMPERSAND
    "apostrophe":                    0x0027,  # U+0027 APOSTROPHE
    "parenleft":                     0x0028,  # U+0028 LEFT PARENTHESIS
    "parenright":                    0x0029,  # U+0029 RIGHT PARENTHESIS
    "asterisk":                      0x002a,  # U+002A ASTERISK
    "plus":                          0x002b,  # U+002B PLUS SIGN
    "comma":                         0x002c,  # U+002C COMMA
    "minus":                         0x002d,  # U+002D HYPHEN-MINUS
    "period":                        0x002e,  # U+002E FULL STOP
    "slash":                         0x002f,  # U+002F SOLIDUS
    "0":                             0x0030,  # U+0030 DIGIT ZERO
    "1":                             0x0031,  # U+0031 DIGIT ONE
    "2":                             0x0032,  # U+0032 DIGIT TWO
    "3":                             0x0033,  # U+0033 DIGIT THREE
    "4":                             0x0034,  # U+0034 DIGIT FOUR
    "5":                             0x0035,  # U+0035 DIGIT FIVE
    "6":                             0x0036,  # U+0036 DIGIT SIX
    "7":                             0x0037,  # U+0037 DIGIT SEVEN
    "8":                             0x0038,  # U+0038 DIGIT EIGHT
    "9":                             0x0039,  # U+0039 DIGIT NINE
    "colon":                         0x003a,  # U+003A COLON
    "semicolon":                     0x003b,  # U+003B SEMICOLON
    "less":                          0x003c,  # U+003C LESS-THAN SIGN
    "equal":                         0x003d,  # U+003D EQUALS SIGN
    "greater":                       0x003e,  # U+003E GREATER-THAN SIGN
    "question":                      0x003f,  # U+003F QUESTION MARK
    "at":                            0x0040,  # U+0040 COMMERCIAL AT
    "A":                             0x0041,  # U+0041 LATIN CAPITAL LETTER A
    "B":                             0x0042,  # U+0042 LATIN CAPITAL LETTER B
    "C":                             0x0043,  # U+0043 LATIN CAPITAL LETTER C
    "D":                             0x0044,  # U+0044 LATIN CAPITAL LETTER D
    "E":                             0x0045,  # U+0045 LATIN CAPITAL LETTER E
    "F":                             0x0046,  # U+0046 LATIN CAPITAL LETTER F
    "G":                             0x0047,  # U+0047 LATIN CAPITAL LETTER G
    "H":                             0x0048,  # U+0048 LATIN CAPITAL LETTER H
    "I":                             0x0049,  # U+0049 LATIN CAPITAL LETTER I
    "J":                             0x004a,  # U+004A LATIN CAPITAL LETTER J
    "K":                             0x004b,  # U+004B LATIN CAPITAL LETTER K
    "L":                             0x004c,  # U+004C LATIN CAPITAL LETTER L
    "M":                             0x004d,  # U+004D LATIN CAPITAL LETTER M
    "N":                             0x004e,  # U+004E LATIN CAPITAL LETTER N
    "O":                             0x004f,  # U+004F LATIN CAPITAL LETTER O
    "P":                             0x0050,  # U+0050 LATIN CAPITAL LETTER P
    "Q":                             0x0051,  # U+0051 LATIN CAPITAL LETTER Q
    "R":                             0x0052,  # U+0052 LATIN CAPITAL LETTER R
    "S":                             0x0053,  # U+0053 LATIN CAPITAL LETTER S
    "T":                             0x0054,  # U+0054 LATIN CAPITAL LETTER T
    "U":                             0x0055,  # U+0055 LATIN CAPITAL LETTER U
    "V":                             0x0056,  # U+0056 LATIN CAPITAL LETTER V
    "W":                             0x0057,  # U+0057 LATIN CAPITAL LETTER W
    "X":                             0x0058,  # U+0058 LATIN CAPITAL LETTER X
    "Y":                             0x0059,  # U+0059 LATIN CAPITAL LETTER Y
    "Z":                             0x005a,  # U+005A LATIN CAPITAL LETTER Z
    "bracketleft":                   0x005b,  # U+005B LEFT SQUARE BRACKET
    "backslash":                     0x005c,  # U+005C REVERSE SOLIDUS
    "bracketright":                  0x005d,  # U+005D RIGHT SQUARE BRACKET
    "asciicircum":                   0x005e,  # U+005E CIRCUMFLEX ACCENT
    "underscore":                    0x005f,  # U+005F LOW LINE
    "grave":                         0x0060,  # U+0060 GRAVE ACCENT
    "a":                             0x0061,  # U+0061 LATIN SMALL LETTER A
    "b":                             0x0062,  # U+0062 LATIN SMALL LETTER B
    "c":                             0x0063,  # U+0063 LATIN SMALL LETTER C
    "d":                             0x0064,  # U+0064 LATIN SMALL LETTER D
    "e":                             0x0065,  # U+0065 LATIN SMALL LETTER E
    "f":                             0x0066,  # U+0066 LATIN SMALL LETTER F
    "g":                             0x0067,  # U+0067 LATIN SMALL LETTER G
    "h":                             0x0068,  # U+0068 LATIN SMALL LETTER H
    "i":                             0x0069,  # U+0069 LATIN SMALL LETTER I
    "j":                             0x006a,  # U+006A LATIN SMALL LETTER J
    "k":                             0x006b,  # U+006B LATIN SMALL LETTER K
    "l":                             0x006c,  # U+006C LATIN SMALL LETTER L
    "m":                             0x006d,  # U+006D LATIN SMALL LETTER M
    "n":                             0x006e,  # U+006E LATIN SMALL LETTER N
    "o":                             0x006f,  # U+006F LATIN SMALL LETTER O
    "p":                             0x0070,  # U+0070 LATIN SMALL LETTER P
    "q":                             0x0071,  # U+0071 LATIN SMALL LETTER Q
    "r":                             0x0072,  # U+0072 LATIN SMALL LETTER R
    "s":                             0x0073,  # U+0073 LATIN SMALL LETTER S
    "t":                             0x0074,  # U+0074 LATIN SMALL LETTER T
    "u":                             0x0075,  # U+0075 LATIN SMALL LETTER U
    "v":                             0x0076,  # U+0076 LATIN SMALL LETTER V
    "w":                             0x0077,  # U+0077 LATIN SMALL LETTER W
    "x":                             0x0078,  # U+0078 LATIN SMALL LETTER X
    "y":                             0x0079,  # U+0079 LATIN SMALL LETTER Y
    "z":                             0x007a,  # U+007A LATIN SMALL LETTER Z
    "braceleft":                     0x007b,  # U+007B LEFT CURLY BRACKET
    "bar":                           0x007c,  # U+007C VERTICAL LINE
    "braceright":                    0x007d,  # U+007D RIGHT CURLY BRACKET
    "asciitilde":                    0x007e,  # U+007E TILDE
    "nobreakspace":                  0x00a0,  # U+00A0 NO-BREAK SPACE
    "exclamdown":                    0x00a1,  # U+00A1 INVERTED EXCLAMATION MARK
    "cent":                          0x00a2,  # U+00A2 CENT SIGN
    "sterling":                      0x00a3,  # U+00A3 POUND SIGN
    "currency":                      0x00a4,  # U+00A4 CURRENCY SIGN
    "yen":                           0x00a5,  # U+00A5 YEN SIGN
    "brokenbar":                     0x00a6,  # U+00A6 BROKEN BAR
    "section":                       0x00a7,  # U+00A7 SECTION SIGN
    "diaeresis":                     0x00a8,  # U+00A8 DIAERESIS
    "copyright":                     0x00a9,  # U+00A9 COPYRIGHT SIGN
    "ordfeminine":                   0x00aa,  # U+00AA FEMININE ORDINAL INDICATOR
    "guillemotleft":                 0x00ab,  # U+00AB LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    "notsign":                       0x00ac,  # U+00AC NOT SIGN
    "hyphen":                        0x00ad,  # U+00AD SOFT HYPHEN
    "registered":                    0x00ae,  # U+00AE REGISTERED SIGN
    "macron":                        0x00af,  # U+00AF MACRON
    "degree":                        0x00b0,  # U+00B0 DEGREE SIGN
    "plusminus":                     0x00b1,  # U+00B1 PLUS-MINUS SIGN
    "twosuperior":                   0x00b2,  # U+00B2 SUPERSCRIPT TWO
    "threesuperior":                 0x00b3,  # U+00B3 SUPERSCRIPT THREE
    "acute":                         0x00b4,  # U+00B4 ACUTE ACCENT
    "mu":                            0x00b5,  # U+00B5 MICRO SIGN
    "paragraph":                     0x00b6,  # U+00B6 PILCROW SIGN
    "periodcentered":                0x00b7,  # U+00B7 MIDDLE DOT
    "cedilla":                       0x00b8,  # U+00B8 CEDILLA
    "onesuperior":                   0x00b9,  # U+00B9 SUPERSCRIPT ONE
    "masculine":                     0x00ba,  # U+00BA MASCULINE ORDINAL INDICATOR
    "guillemotright":                0x00bb,  # U+00BB RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    "onequarter":                    0x00bc,  # U+00BC VULGAR FRACTION ONE QUARTER
    "onehalf":                       0x00bd,  # U+00BD VULGAR FRACTION ONE HALF
    "threequarters":                 0x00be,  # U+00BE VULGAR FRACTION THREE QUARTERS
    "questiondown":                  0x00bf,  # U+00BF INVERTED QUESTION MARK
    "Agrave":                        0x00c0,  # U+00C0 LATIN CAPITAL LETTER A WITH GRAVE
    "Aacute":                        0x00c1,  # U+00C1 LATIN CAPITAL LETTER A WITH ACUTE
    "Acircumflex":                   0x00c2,  # U+00C2 LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    "Atilde":                        0x00c3,  # U+00C3 LATIN CAPITAL LETTER A WITH TILDE
    "Adiaeresis":                    0x00c4,  # U+00C4 LATIN CAPITAL LETTER A WITH DIAERESIS
    "Aring":                         0x00c5,  # U+00C5 LATIN CAPITAL LETTER A WITH RING ABOVE
    "AE":                            0x00c6,  # U+00C6 LATIN CAPITAL LETTER AE
    "Ccedilla":                      0x00c7,  # U+00C7 LATIN CAPITAL LETTER C WITH CEDILLA
    "Egrave":                        0x00c8,  # U+00C8 LATIN CAPITAL LETTER E WITH GRAVE
    "Eacute":                        0x00c9,  # U+00C9 LATIN CAPITAL LETTER E WITH ACUTE
    "Ecircumflex":                   0x00ca,  # U+00CA LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    "Ediaeresis":                    0x00cb,  # U+00CB LATIN CAPITAL LETTER E WITH DIAERESIS
    "Igrave":                        0x00cc,  # U+00CC LATIN CAPITAL LETTER I WITH GRAVE
    "Iacute":                        0x00cd,  # U+00CD LATIN CAPITAL LETTER I WITH ACUTE
    "Icircumflex":                   0x00ce,  # U+00CE LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    "Idiaeresis":                    0x00cf,  # U+00CF LATIN CAPITAL LETTER I WITH DIAERESIS
    "ETH":                           0x00d0,  # U+00D0 LATIN CAPITAL LETTER ETH
    "Ntilde":                        0x00d1,  # U+00D1 LATIN CAPITAL LETTER N WITH TILDE
    "Ograve":                        0x00d2,  # U+00D2 LATIN CAPITAL LETTER O WITH GRAVE
    "Oacute":                        0x00d3,  # U+00D3 LATIN CAPITAL LETTER O WITH ACUTE
    "Ocircumflex":                   0x00d4,  # U+00D4 LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    "Otilde":                        0x00d5,  # U+00D5 LATIN CAPITAL LETTER O WITH TILDE
    "Odiaeresis":                    0x00d6,  # U+00D6 LATIN CAPITAL LETTER O WITH DIAERESIS
    "multiply":                      0x00d7,  # U+00D7 MULTIPLICATION SIGN
    "Oslash":                        0x00d8,  # U+00D8 LATIN CAPITAL LETTER O WITH STROKE
    "Ooblique":                      0x00d8,  # U+00D8 LATIN CAPITAL LETTER O WITH STROKE
    "Ugrave":                        0x00d9,  # U+00D9 LATIN CAPITAL LETTER U WITH GRAVE
    "Uacute":                        0x00da,  # U+00DA LATIN CAPITAL LETTER U WITH ACUTE
    "Ucircumflex":                   0x00db,  # U+00DB LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    "Udiaeresis":                    0x00dc,  # U+00DC LATIN CAPITAL LETTER U WITH DIAERESIS
    "Yacute":                        0x00dd,  # U+00DD LATIN CAPITAL LETTER Y WITH ACUTE
    "THORN":                         0x00de,  # U+00DE LATIN CAPITAL LETTER THORN
    "ssharp":                        0x00df,  # U+00DF LATIN SMALL LETTER SHARP S
    "agrave":                        0x00e0,  # U+00E0 LATIN SMALL LETTER A WITH GRAVE
    "aacute":                        0x00e1,  # U+00E1 LATIN SMALL LETTER A WITH ACUTE
    "acircumflex":                   0x00e2,  # U+00E2 LATIN SMALL LETTER A WITH CIRCUMFLEX
    "atilde":                        0x00e3,  # U+00E3 LATIN SMALL LETTER A WITH TILDE
    "adiaeresis":                    0x00e4,  # U+00E4 LATIN SMALL LETTER A WITH DIAERESIS
    "aring":                         0x00e5,  # U+00E5 LATIN SMALL LETTER A WITH RING ABOVE
    "ae":                            0x00e6,  # U+00E6 LATIN SMALL LETTER AE
    "ccedilla":                      0x00e7,  # U+00E7 LATIN SMALL LETTER C WITH CEDILLA
    "egrave":                        0x00e8,  # U+00E8 LATIN SMALL LETTER E WITH GRAVE
    "eacute":                        0x00e9,  # U+00E9 LATIN SMALL LETTER E WITH ACUTE
    "ecircumflex":                   0x00ea,  # U+00EA LATIN SMALL LETTER E WITH CIRCUMFLEX
    "ediaeresis":                    0x00eb,  # U+00EB LATIN SMALL LETTER E WITH DIAERESIS
    "igrave":                        0x00ec,  # U+00EC LATIN SMALL LETTER I WITH GRAVE
    "iacute":                        0x00ed,  # U+00ED LATIN SMALL LETTER I WITH ACUTE
    "icircumflex":                   0x00ee,  # U+00EE LATIN SMALL LETTER I WITH CIRCUMFLEX
    "idiaeresis":                    0x00ef,  # U+00EF LATIN SMALL LETTER I WITH DIAERESIS
    "eth":                           0x00f0,  # U+00F0 LATIN SMALL LETTER ETH
    "ntilde":                        0x00f1,  # U+00F1 LATIN SMALL LETTER N WITH TILDE
    "ograve":                        0x00f2,  # U+00F2 LATIN SMALL LETTER O WITH GRAVE
    "oacute":                        0x00f3,  # U+00F3 LATIN SMALL LETTER O WITH ACUTE
    "ocircumflex":                   0x00f4,  # U+00F4 LATIN SMALL LETTER O WITH CIRCUMFLEX
    "otilde":                        0x00f5,  # U+00F5 LATIN SMALL LETTER O WITH TILDE
    "odiaeresis":                    0x00f6,  # U+00F6 LATIN SMALL LETTER O WITH DIAERESIS
    "division":                      0x00f7,  # U+00F7 DIVISION SIGN
    "oslash":                        0x00f8,  # U+00F8 LATIN SMALL LETTER O WITH STROKE
    "ooblique":                      0x00f8,  # U+00F8 LATIN SMALL LETTER O WITH STROKE
    "ugrave":                        0x00f9,  # U+00F9 LATIN SMALL LETTER U WITH GRAVE
    "uacute":                        0x00fa,  # U+00FA LATIN SMALL LETTER U WITH ACUTE
    "ucircumflex":                   0x00fb,  # U+00FB LATIN SMALL LETTER U WITH CIRCUMFLEX
    "udiaeresis":                    0x00fc,  # U+00FC LATIN SMALL LETTER U WITH DIAERESIS
    "yacute":                        0x00fd,  # U+00FD LATIN SMALL LETTER Y WITH ACUTE
    "thorn":                         0x00fe,  # U+00FE LATIN SMALL LETTER THORN
    "ydiaeresis":                    0x00ff,  # U+00FF LATIN SMALL LETTER Y WITH DIAERESIS
    "Aogonek":                       0x01a1,  # U+0104 LATIN CAPITAL LETTER A WITH OGONEK
    "breve":                         0x01a2,  # U+02D8 BREVE
    "Lstroke":                       0x01a3,  # U+0141 LATIN CAPITAL LETTER L WITH STROKE
    "Lcaron":                        0x01a5,  # U+013D LATIN CAPITAL LETTER L WITH CARON
    "Sacute":                        0x01a6,  # U+015A LATIN CAPITAL LETTER S WITH ACUTE
    "Scaron":                        0x01a9,  # U+0160 LATIN CAPITAL LETTER S WITH CARON
    "Scedilla":                      0x01aa,  # U+015E LATIN CAPITAL LETTER S WITH CEDILLA
    "Tcaron":                        0x01ab,  # U+0164 LATIN CAPITAL LETTER T WITH CARON
    "Zacute":                        0x01ac,  # U+0179 LATIN CAPITAL LETTER Z WITH ACUTE
    "Zcaron":                        0x01ae,  # U+017D LATIN CAPITAL LETTER Z WITH CARON
    "Zabovedot":                     0x01af,  # U+017B LATIN CAPITAL LETTER Z WITH DOT ABOVE
    "aogonek":                       0x01b1,  # U+0105 LATIN SMALL LETTER A WITH OGONEK
    "ogonek":                        0x01b2,  # U+02DB OGONEK
    "lstroke":                       0x01b3,  # U+0142 LATIN SMALL LETTER L WITH STROKE
    "lcaron":                        0x01b5,  # U+013E LATIN SMALL LETTER L WITH CARON
    "sacute":                        0x01b6,  # U+015B LATIN SMALL LETTER S WITH ACUTE
    "caron":                         0x01b7,  # U+02C7 CARON
    "scaron":                        0x01b9,  # U+0161 LATIN SMALL LETTER S WITH CARON
    "scedilla":                      0x01ba,  # U+015F LATIN SMALL LETTER S WITH CEDILLA
    "tcaron":                        0x01bb,  # U+0165 LATIN SMALL LETTER T WITH CARON
    "zacute":                        0x01bc,  # U+017A LATIN SMALL LETTER Z WITH ACUTE
    "doubleacute":                   0x01bd,  # U+02DD DOUBLE ACUTE ACCENT
    "zcaron":                        0x01be,  # U+017E LATIN SMALL LETTER Z WITH CARON
    "zabovedot":                     0x01bf,  # U+017C LATIN SMALL LETTER Z WITH DOT ABOVE
    "Racute":                        0x01c0,  # U+0154 LATIN CAPITAL LETTER R WITH ACUTE
    "Abreve":                        0x01c3,  # U+0102 LATIN CAPITAL LETTER A WITH BREVE
    "Lacute":                        0x01c5,  # U+0139 LATIN CAPITAL LETTER L WITH ACUTE
    "Cacute":                        0x01c6,  # U+0106 LATIN CAPITAL LETTER C WITH ACUTE
    "Ccaron":                        0x01c8,  # U+010C LATIN CAPITAL LETTER C WITH CARON
    "Eogonek":                       0x01ca,  # U+0118 LATIN CAPITAL LETTER E WITH OGONEK
    "Ecaron":                        0x01cc,  # U+011A LATIN CAPITAL LETTER E WITH CARON
    "Dcaron":                        0x01cf,  # U+010E LATIN CAPITAL LETTER D WITH CARON
    "Dstroke":                       0x01d0,  # U+0110 LATIN CAPITAL LETTER D WITH STROKE
    "Nacute":                        0x01d1,  # U+0143 LATIN CAPITAL LETTER N WITH ACUTE
    "Ncaron":                        0x01d2,  # U+0147 LATIN CAPITAL LETTER N WITH CARON
    "Odoubleacute":                  0x01d5,  # U+0150 LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
    "Rcaron":                        0x01d8,  # U+0158 LATIN CAPITAL LETTER R WITH CARON
    "Uring":                         0x01d9,  # U+016E LATIN CAPITAL LETTER U WITH RING ABOVE
    "Udoubleacute":                  0x01db,  # U+0170 LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
    "Tcedilla":                      0x01de,  # U+0162 LATIN CAPITAL LETTER T WITH CEDILLA
    "racute":                        0x01e0,  # U+0155 LATIN SMALL LETTER R WITH ACUTE
    "abreve":                        0x01e3,  # U+0103 LATIN SMALL LETTER A WITH BREVE
    "lacute":                        0x01e5,  # U+013A LATIN SMALL LETTER L WITH ACUTE
    "cacute":                        0x01e6,  # U+0107 LATIN SMALL LETTER C WITH ACUTE
    "ccaron":                        0x01e8,  # U+010D LATIN SMALL LETTER C WITH CARON
    "eogonek":                       0x01ea,  # U+0119 LATIN SMALL LETTER E WITH OGONEK
    "ecaron":                        0x01ec,  # U+011B LATIN SMALL LETTER E WITH CARON
    "dcaron":                        0x01ef,  # U+010F LATIN SMALL LETTER D WITH CARON
    "dstroke":                       0x01f0,  # U+0111 LATIN SMALL LETTER D WITH STROKE
    "nacute":                        0x01f1,  # U+0144 LATIN SMALL LETTER N WITH ACUTE
    "ncaron":                        0x01f2,  # U+0148 LATIN SMALL LETTER N WITH CARON
    "odoubleacute":                  0x01f5,  # U+0151 LATIN SMALL LETTER O WITH DOUBLE ACUTE
    "rcaron":                        0x01f8,  # U+0159 LATIN SMALL LETTER R WITH CARON
    "uring":                         0x01f9,  # U+016F LATIN SMALL LETTER U WITH RING ABOVE
    "udoubleacute":                  0x01fb,  # U+0171 LATIN SMALL LETTER U WITH DOUBLE ACUTE
    "tcedilla":                      0x01fe,  # U+0163 LATIN SMALL LETTER T WITH CEDILLA
    "abovedot":                      0x01ff,  # U+02D9 DOT ABOVE
    "Hstroke":                       0x02a1,  # U+0126 LATIN CAPITAL LETTER H WITH STROKE
    "Hcircumflex":                   0x02a6,  # U+0124 LATIN CAPITAL LETTER H WITH CIRCUMFLEX
    "Iabovedot":                     0x02a9,  # U+0130 LATIN CAPITAL LETTER I WITH DOT ABOVE
    "Gbreve":                        0x02ab,  # U+011E LATIN CAPITAL LETTER G WITH BREVE
    "Jcircumflex":                   0x02ac,  # U+0134 LATIN CAPITAL LETTER J WITH CIRCUMFLEX
    "hstroke":                       0x02b1,  # U+0127 LATIN SMALL LETTER H WITH STROKE
    "hcircumflex":                   0x02b6,  # U+0125 LATIN SMALL LETTER H WITH CIRCUMFLEX
    "idotless":                      0x02b9,  # U+0131 LATIN SMALL LETTER DOTLESS I
    "gbreve":                        0x02bb,  # U+011F LATIN SMALL LETTER G WITH BREVE
    "jcircumflex":                   0x02bc,  # U+0135 LATIN SMALL LETTER J WITH CIRCUMFLEX
    "Cabovedot":                     0x02c5,  # U+010A LATIN CAPITAL LETTER C WITH DOT ABOVE
    "Ccircumflex":                   0x02c6,  # U+0108 LATIN CAPITAL LETTER C WITH CIRCUMFLEX
    "Gabovedot":                     0x02d5,  # U+0120 LATIN CAPITAL LETTER G WITH DOT ABOVE
    "Gcircumflex":                   0x02d8,  # U+011C LATIN CAPITAL LETTER G WITH CIRCUMFLEX
    "Ubreve":                        0x02dd,  # U+016C LATIN CAPITAL LETTER U WITH BREVE
    "Scircumflex":                   0x02de,  # U+015C LATIN CAPITAL LETTER S WITH CIRCUMFLEX
    "cabovedot":                     0x02e5,  # U+010B LATIN SMALL LETTER C WITH DOT ABOVE
    "ccircumflex":                   0x02e6,  # U+0109 LATIN SMALL LETTER C WITH CIRCUMFLEX
    "gabovedot":                     0x02f5,  # U+0121 LATIN SMALL LETTER G WITH DOT ABOVE
    "gcircumflex":                   0x02f8,  # U+011D LATIN SMALL LETTER G WITH CIRCUMFLEX
    "ubreve":                        0x02fd,  # U+016D LATIN SMALL LETTER U WITH BREVE
    "scircumflex":                   0x02fe,  # U+015D LATIN SMALL LETTER S WITH CIRCUMFLEX
    "kra":                           0x03a2,  # U+0138 LATIN SMALL LETTER KRA
    "Rcedilla":                      0x03a3,  # U+0156 LATIN CAPITAL LETTER R WITH CEDILLA
    "Itilde":                        0x03a5,  # U+0128 LATIN CAPITAL LETTER I WITH TILDE
    "Lcedilla":                      0x03a6,  # U+013B LATIN CAPITAL LETTER L WITH CEDILLA
    "Emacron":                       0x03aa,  # U+0112 LATIN CAPITAL LETTER E WITH MACRON
    "Gcedilla":                      0x03ab,  # U+0122 LATIN CAPITAL LETTER G WITH CEDILLA
    "Tslash":                        0x03ac,  # U+0166 LATIN CAPITAL LETTER T WITH STROKE
    "rcedilla":                      0x03b3,  # U+0157 LATIN SMALL LETTER R WITH CEDILLA
    "itilde":                        0x03b5,  # U+0129 LATIN SMALL LETTER I WITH TILDE
    "lcedilla":                      0x03b6,  # U+013C LATIN SMALL LETTER L WITH CEDILLA
    "emacron":                       0x03ba,  # U+0113 LATIN SMALL LETTER E WITH MACRON
    "gcedilla":                      0x03bb,  # U+0123 LATIN SMALL LETTER G WITH CEDILLA
    "tslash":                        0x03bc,  # U+0167 LATIN SMALL LETTER T WITH STROKE
    "ENG":                           0x03bd,  # U+014A LATIN CAPITAL LETTER ENG
    "eng":                           0x03bf,  # U+014B LATIN SMALL LETTER ENG
    "Amacron":                       0x03c0,  # U+0100 LATIN CAPITAL LETTER A WITH MACRON
    "Iogonek":                       0x03c7,  # U+012E LATIN CAPITAL LETTER I WITH OGONEK
    "Eabovedot":                     0x03cc,  # U+0116 LATIN CAPITAL LETTER E WITH DOT ABOVE
    "Imacron":                       0x03cf,  # U+012A LATIN CAPITAL LETTER I WITH MACRON
    "Ncedilla":                      0x03d1,  # U+0145 LATIN CAPITAL LETTER N WITH CEDILLA
    "Omacron":                       0x03d2,  # U+014C LATIN CAPITAL LETTER O WITH MACRON
    "Kcedilla":                      0x03d3,  # U+0136 LATIN CAPITAL LETTER K WITH CEDILLA
    "Uogonek":                       0x03d9,  # U+0172 LATIN CAPITAL LETTER U WITH OGONEK
    "Utilde":                        0x03dd,  # U+0168 LATIN CAPITAL LETTER U WITH TILDE
    "Umacron":                       0x03de,  # U+016A LATIN CAPITAL LETTER U WITH MACRON
    "amacron":                       0x03e0,  # U+0101 LATIN SMALL LETTER A WITH MACRON
    "iogonek":                       0x03e7,  # U+012F LATIN SMALL LETTER I WITH OGONEK
    "eabovedot":                     0x03ec,  # U+0117 LATIN SMALL LETTER E WITH DOT ABOVE
    "imacron":                       0x03ef,  # U+012B LATIN SMALL LETTER I WITH MACRON
    "ncedilla":                      0x03f1,  # U+0146 LATIN SMALL LETTER N WITH CEDILLA
    "omacron":                       0x03f2,  # U+014D LATIN SMALL LETTER O WITH MACRON
    "kcedilla":                      0x03f3,  # U+0137 LATIN SMALL LETTER K WITH CEDILLA
    "uogonek":                       0x03f9,  # U+0173 LATIN SMALL LETTER U WITH OGONEK
    "utilde":                        0x03fd,  # U+0169 LATIN SMALL LETTER U WITH TILDE
    "umacron":                       0x03fe,  # U+016B LATIN SMALL LETTER U WITH MACRON
    "Wcircumflex":                0x1000174,  # U+0174 LATIN CAPITAL LETTER W WITH CIRCUMFLEX
    "wcircumflex":                0x1000175,  # U+0175 LATIN SMALL LETTER W WITH CIRCUMFLEX
    "Ycircumflex":                0x1000176,  # U+0176 LATIN CAPITAL LETTER Y WITH CIRCUMFLEX
    "ycircumflex":                0x1000177,  # U+0177 LATIN SMALL LETTER Y WITH CIRCUMFLEX
    "Babovedot":                  0x1001e02,  # U+1E02 LATIN CAPITAL LETTER B WITH DOT ABOVE
    "babovedot":                  0x1001e03,  # U+1E03 LATIN SMALL LETTER B WITH DOT ABOVE
    "Dabovedot":                  0x1001e0a,  # U+1E0A LATIN CAPITAL LETTER D WITH DOT ABOVE
    "dabovedot":                  0x1001e0b,  # U+1E0B LATIN SMALL LETTER D WITH DOT ABOVE
    "Fabovedot":                  0x1001e1e,  # U+1E1E LATIN CAPITAL LETTER F WITH DOT ABOVE
    "fabovedot":                  0x1001e1f,  # U+1E1F LATIN SMALL LETTER F WITH DOT ABOVE
    "Mabovedot":                  0x1001e40,  # U+1E40 LATIN CAPITAL LETTER M WITH DOT ABOVE
    "mabovedot":                  0x1001e41,  # U+1E41 LATIN SMALL LETTER M WITH DOT ABOVE
    "Pabovedot":                  0x1001e56,  # U+1E56 LATIN CAPITAL LETTER P WITH DOT ABOVE
    "pabovedot":                  0x1001e57,  # U+1E57 LATIN SMALL LETTER P WITH DOT ABOVE
    "Sabovedot":                  0x1001e60,  # U+1E60 LATIN CAPITAL LETTER S WITH DOT ABOVE
    "sabovedot":                  0x1001e61,  # U+1E61 LATIN SMALL LETTER S WITH DOT ABOVE
    "Tabovedot":                  0x1001e6a,  # U+1E6A LATIN CAPITAL LETTER T WITH DOT ABOVE
    "tabovedot":                  0x1001e6b,  # U+1E6B LATIN SMALL LETTER T WITH DOT ABOVE
    "Wgrave":                     0x1001e80,  # U+1E80 LATIN CAPITAL LETTER W WITH GRAVE
    "wgrave":                     0x1001e81,  # U+1E81 LATIN SMALL LETTER W WITH GRAVE
    "Wacute":                     0x1001e82,  # U+1E82 LATIN CAPITAL LETTER W WITH ACUTE
    "wacute":                     0x1001e83,  # U+1E83 LATIN SMALL LETTER W WITH ACUTE
    "Wdiaeresis":                 0x1001e84,  # U+1E84 LATIN CAPITAL LETTER W WITH DIAERESIS
    "wdiaeresis":                 0x1001e85,  # U+1E85 LATIN SMALL LETTER W WITH DIAERESIS
    "Ygrave":                     0x1001ef2,  # U+1EF2 LATIN CAPITAL LETTER Y WITH GRAVE
    "ygrave":                     0x1001ef3,  # U+1EF3 LATIN SMALL LETTER Y WITH GRAVE
    "OE":                            0x13bc,  # U+0152 LATIN CAPITAL LIGATURE OE
    "oe":                            0x13bd,  # U+0153 LATIN SMALL LIGATURE OE
    "Ydiaeresis":                    0x13be,  # U+0178 LATIN CAPITAL LETTER Y WITH DIAERESIS
    "overline":                      0x047e,  # U+203E OVERLINE
    "kana_fullstop":                 0x04a1,  # U+3002 IDEOGRAPHIC FULL STOP
    "kana_openingbracket":           0x04a2,  # U+300C LEFT CORNER BRACKET
    "kana_closingbracket":           0x04a3,  # U+300D RIGHT CORNER BRACKET
    "kana_comma":                    0x04a4,  # U+3001 IDEOGRAPHIC COMMA
    "kana_conjunctive":              0x04a5,  # U+30FB KATAKANA MIDDLE DOT
    "kana_WO":                       0x04a6,  # U+30F2 KATAKANA LETTER WO
    "kana_a":                        0x04a7,  # U+30A1 KATAKANA LETTER SMALL A
    "kana_i":                        0x04a8,  # U+30A3 KATAKANA LETTER SMALL I
    "kana_u":                        0x04a9,  # U+30A5 KATAKANA LETTER SMALL U
    "kana_e":                        0x04aa,  # U+30A7 KATAKANA LETTER SMALL E
    "kana_o":                        0x04ab,  # U+30A9 KATAKANA LETTER SMALL O
    "kana_ya":                       0x04ac,  # U+30E3 KATAKANA LETTER SMALL YA
    "kana_yu":                       0x04ad,  # U+30E5 KATAKANA LETTER SMALL YU
    "kana_yo":                       0x04ae,  # U+30E7 KATAKANA LETTER SMALL YO
    "kana_tsu":                      0x04af,  # U+30C3 KATAKANA LETTER SMALL TU
    "prolongedsound":                0x04b0,  # U+30FC KATAKANA-HIRAGANA PROLONGED SOUND MARK
    "kana_A":                        0x04b1,  # U+30A2 KATAKANA LETTER A
    "kana_I":                        0x04b2,  # U+30A4 KATAKANA LETTER I
    "kana_U":                        0x04b3,  # U+30A6 KATAKANA LETTER U
    "kana_E":                        0x04b4,  # U+30A8 KATAKANA LETTER E
    "kana_O":                        0x04b5,  # U+30AA KATAKANA LETTER O
    "kana_KA":                       0x04b6,  # U+30AB KATAKANA LETTER KA
    "kana_KI":                       0x04b7,  # U+30AD KATAKANA LETTER KI
    "kana_KU":                       0x04b8,  # U+30AF KATAKANA LETTER KU
    "kana_KE":                       0x04b9,  # U+30B1 KATAKANA LETTER KE
    "kana_KO":                       0x04ba,  # U+30B3 KATAKANA LETTER KO
    "kana_SA":                       0x04bb,  # U+30B5 KATAKANA LETTER SA
    "kana_SHI":                      0x04bc,  # U+30B7 KATAKANA LETTER SI
    "kana_SU":                       0x04bd,  # U+30B9 KATAKANA LETTER SU
    "kana_SE":                       0x04be,  # U+30BB KATAKANA LETTER SE
    "kana_SO":                       0x04bf,  # U+30BD KATAKANA LETTER SO
    "kana_TA":                       0x04c0,  # U+30BF KATAKANA LETTER TA
    "kana_CHI":                      0x04c1,  # U+30C1 KATAKANA LETTER TI
    "kana_TSU":                      0x04c2,  # U+30C4 KATAKANA LETTER TU
    "kana_TE":                       0x04c3,  # U+30C6 KATAKANA LETTER TE
    "kana_TO":                       0x04c4,  # U+30C8 KATAKANA LETTER TO
    "kana_NA":                       0x04c5,  # U+30CA KATAKANA LETTER NA
    "kana_NI":                       0x04c6,  # U+30CB KATAKANA LETTER NI
    "kana_NU":                       0x04c7,  # U+30CC KATAKANA LETTER NU
    "kana_NE":                       0x04c8,  # U+30CD KATAKANA LETTER NE
    "kana_NO":                       0x04c9,  # U+30CE KATAKANA LETTER NO
    "kana_HA":                       0x04ca,  # U+30CF KATAKANA LETTER HA
    "kana_HI":                       0x04cb,  # U+30D2 KATAKANA LETTER HI
    "kana_FU":                       0x04cc,  # U+30D5 KATAKANA LETTER HU
    "kana_HE":                       0x04cd,  # U+30D8 KATAKANA LETTER HE
    "kana_HO":                       0x04ce,  # U+30DB KATAKANA LETTER HO
    "kana_MA":                       0x04cf,  # U+30DE KATAKANA LETTER MA
    "kana_MI":                       0x04d0,  # U+30DF KATAKANA LETTER MI
    "kana_MU":                       0x04d1,  # U+30E0 KATAKANA LETTER MU
    "kana_ME":                       0x04d2,  # U+30E1 KATAKANA LETTER ME
    "kana_MO":                       0x04d3,  # U+30E2 KATAKANA LETTER MO
    "kana_YA":                       0x04d4,  # U+30E4 KATAKANA LETTER YA
    "kana_YU":                       0x04d5,  # U+30E6 KATAKANA LETTER YU
    "kana_YO":                       0x04d6,  # U+30E8 KATAKANA LETTER YO
    "kana_RA":                       0x04d7,  # U+30E9 KATAKANA LETTER RA
    "kana_RI":                       0x04d8,  # U+30EA KATAKANA LETTER RI
    "kana_RU":                       0x04d9,  # U+30EB KATAKANA LETTER RU
    "kana_RE":                       0x04da,  # U+30EC KATAKANA LETTER RE
    "kana_RO":                       0x04db,  # U+30ED KATAKANA LETTER RO
    "kana_WA":                       0x04dc,  # U+30EF KATAKANA LETTER WA
    "kana_N":                        0x04dd,  # U+30F3 KATAKANA LETTER N
    "voicedsound":                   0x04de,  # U+309B KATAKANA-HIRAGANA VOICED SOUND MARK
    "semivoicedsound":               0x04df,  # U+309C KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK
    "kana_switch":                   0xff7e,  # Alias for mode_switch
    "Farsi_0":                    0x10006f0,  # U+06F0 EXTENDED ARABIC-INDIC DIGIT ZERO
    "Farsi_1":                    0x10006f1,  # U+06F1 EXTENDED ARABIC-INDIC DIGIT ONE
    "Farsi_2":                    0x10006f2,  # U+06F2 EXTENDED ARABIC-INDIC DIGIT TWO
    "Farsi_3":                    0x10006f3,  # U+06F3 EXTENDED ARABIC-INDIC DIGIT THREE
    "Farsi_4":                    0x10006f4,  # U+06F4 EXTENDED ARABIC-INDIC DIGIT FOUR
    "Farsi_5":                    0x10006f5,  # U+06F5 EXTENDED ARABIC-INDIC DIGIT FIVE
    "Farsi_6":                    0x10006f6,  # U+06F6 EXTENDED ARABIC-INDIC DIGIT SIX
    "Farsi_7":                    0x10006f7,  # U+06F7 EXTENDED ARABIC-INDIC DIGIT SEVEN
    "Farsi_8":                    0x10006f8,  # U+06F8 EXTENDED ARABIC-INDIC DIGIT EIGHT
    "Farsi_9":                    0x10006f9,  # U+06F9 EXTENDED ARABIC-INDIC DIGIT NINE
    "Arabic_percent":             0x100066a,  # U+066A ARABIC PERCENT SIGN
    "Arabic_superscript_alef":    0x1000670,  # U+0670 ARABIC LETTER SUPERSCRIPT ALEF
    "Arabic_tteh":                0x1000679,  # U+0679 ARABIC LETTER TTEH
    "Arabic_peh":                 0x100067e,  # U+067E ARABIC LETTER PEH
    "Arabic_tcheh":               0x1000686,  # U+0686 ARABIC LETTER TCHEH
    "Arabic_ddal":                0x1000688,  # U+0688 ARABIC LETTER DDAL
    "Arabic_rreh":                0x1000691,  # U+0691 ARABIC LETTER RREH
    "Arabic_comma":                  0x05ac,  # U+060C ARABIC COMMA
    "Arabic_fullstop":            0x10006d4,  # U+06D4 ARABIC FULL STOP
    "Arabic_0":                   0x1000660,  # U+0660 ARABIC-INDIC DIGIT ZERO
    "Arabic_1":                   0x1000661,  # U+0661 ARABIC-INDIC DIGIT ONE
    "Arabic_2":                   0x1000662,  # U+0662 ARABIC-INDIC DIGIT TWO
    "Arabic_3":                   0x1000663,  # U+0663 ARABIC-INDIC DIGIT THREE
    "Arabic_4":                   0x1000664,  # U+0664 ARABIC-INDIC DIGIT FOUR
    "Arabic_5":                   0x1000665,  # U+0665 ARABIC-INDIC DIGIT FIVE
    "Arabic_6":                   0x1000666,  # U+0666 ARABIC-INDIC DIGIT SIX
    "Arabic_7":                   0x1000667,  # U+0667 ARABIC-INDIC DIGIT SEVEN
    "Arabic_8":                   0x1000668,  # U+0668 ARABIC-INDIC DIGIT EIGHT
    "Arabic_9":                   0x1000669,  # U+0669 ARABIC-INDIC DIGIT NINE
    "Arabic_semicolon":              0x05bb,  # U+061B ARABIC SEMICOLON
    "Arabic_question_mark":          0x05bf,  # U+061F ARABIC QUESTION MARK
    "Arabic_hamza":                  0x05c1,  # U+0621 ARABIC LETTER HAMZA
    "Arabic_maddaonalef":            0x05c2,  # U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE
    "Arabic_hamzaonalef":            0x05c3,  # U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE
    "Arabic_hamzaonwaw":             0x05c4,  # U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE
    "Arabic_hamzaunderalef":         0x05c5,  # U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW
    "Arabic_hamzaonyeh":             0x05c6,  # U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE
    "Arabic_alef":                   0x05c7,  # U+0627 ARABIC LETTER ALEF
    "Arabic_beh":                    0x05c8,  # U+0628 ARABIC LETTER BEH
    "Arabic_tehmarbuta":             0x05c9,  # U+0629 ARABIC LETTER TEH MARBUTA
    "Arabic_teh":                    0x05ca,  # U+062A ARABIC LETTER TEH
    "Arabic_theh":                   0x05cb,  # U+062B ARABIC LETTER THEH
    "Arabic_jeem":                   0x05cc,  # U+062C ARABIC LETTER JEEM
    "Arabic_hah":                    0x05cd,  # U+062D ARABIC LETTER HAH
    "Arabic_khah":                   0x05ce,  # U+062E ARABIC LETTER KHAH
    "Arabic_dal":                    0x05cf,  # U+062F ARABIC LETTER DAL
    "Arabic_thal":                   0x05d0,  # U+0630 ARABIC LETTER THAL
    "Arabic_ra":                     0x05d1,  # U+0631 ARABIC LETTER REH
    "Arabic_zain":                   0x05d2,  # U+0632 ARABIC LETTER ZAIN
    "Arabic_seen":                   0x05d3,  # U+0633 ARABIC LETTER SEEN
    "Arabic_sheen":                  0x05d4,  # U+0634 ARABIC LETTER SHEEN
    "Arabic_sad":                    0x05d5,  # U+0635 ARABIC LETTER SAD
    "Arabic_dad":                    0x05d6,  # U+0636 ARABIC LETTER DAD
    "Arabic_tah":                    0x05d7,  # U+0637 ARABIC LETTER TAH
    "Arabic_zah":                    0x05d8,  # U+0638 ARABIC LETTER ZAH
    "Arabic_ain":                    0x05d9,  # U+0639 ARABIC LETTER AIN
    "Arabic_ghain":                  0x05da,  # U+063A ARABIC LETTER GHAIN
    "Arabic_tatweel":                0x05e0,  # U+0640 ARABIC TATWEEL
    "Arabic_feh":                    0x05e1,  # U+0641 ARABIC LETTER FEH
    "Arabic_qaf":                    0x05e2,  # U+0642 ARABIC LETTER QAF
    "Arabic_kaf":                    0x05e3,  # U+0643 ARABIC LETTER KAF
    "Arabic_lam":                    0x05e4,  # U+0644 ARABIC LETTER LAM
    "Arabic_meem":                   0x05e5,  # U+0645 ARABIC LETTER MEEM
    "Arabic_noon":                   0x05e6,  # U+0646 ARABIC LETTER NOON
    "Arabic_ha":                     0x05e7,  # U+0647 ARABIC LETTER HEH
    "Arabic_waw":                    0x05e8,  # U+0648 ARABIC LETTER WAW
    "Arabic_alefmaksura":            0x05e9,  # U+0649 ARABIC LETTER ALEF MAKSURA
    "Arabic_yeh":                    0x05ea,  # U+064A ARABIC LETTER YEH
    "Arabic_fathatan":               0x05eb,  # U+064B ARABIC FATHATAN
    "Arabic_dammatan":               0x05ec,  # U+064C ARABIC DAMMATAN
    "Arabic_kasratan":               0x05ed,  # U+064D ARABIC KASRATAN
    "Arabic_fatha":                  0x05ee,  # U+064E ARABIC FATHA
    "Arabic_damma":                  0x05ef,  # U+064F ARABIC DAMMA
    "Arabic_kasra":                  0x05f0,  # U+0650 ARABIC KASRA
    "Arabic_shadda":                 0x05f1,  # U+0651 ARABIC SHADDA
    "Arabic_sukun":                  0x05f2,  # U+0652 ARABIC SUKUN
    "Arabic_madda_above":         0x1000653,  # U+0653 ARABIC MADDAH ABOVE
    "Arabic_hamza_above":         0x1000654,  # U+0654 ARABIC HAMZA ABOVE
    "Arabic_hamza_below":         0x1000655,  # U+0655 ARABIC HAMZA BELOW
    "Arabic_jeh":                 0x1000698,  # U+0698 ARABIC LETTER JEH
    "Arabic_veh":                 0x10006a4,  # U+06A4 ARABIC LETTER VEH
    "Arabic_keheh":               0x10006a9,  # U+06A9 ARABIC LETTER KEHEH
    "Arabic_gaf":                 0x10006af,  # U+06AF ARABIC LETTER GAF
    "Arabic_noon_ghunna":         0x10006ba,  # U+06BA ARABIC LETTER NOON GHUNNA
    "Arabic_heh_doachashmee":     0x10006be,  # U+06BE ARABIC LETTER HEH DOACHASHMEE
    "Farsi_yeh":                  0x10006cc,  # U+06CC ARABIC LETTER FARSI YEH
    "Arabic_farsi_yeh":           0x10006cc,  # U+06CC ARABIC LETTER FARSI YEH
    "Arabic_yeh_baree":           0x10006d2,  # U+06D2 ARABIC LETTER YEH BARREE
    "Arabic_heh_goal":            0x10006c1,  # U+06C1 ARABIC LETTER HEH GOAL
    "Arabic_switch":                 0xff7e,  # Alias for mode_switch
    "Cyrillic_GHE_bar":           0x1000492,  # U+0492 CYRILLIC CAPITAL LETTER GHE WITH STROKE
    "Cyrillic_ghe_bar":           0x1000493,  # U+0493 CYRILLIC SMALL LETTER GHE WITH STROKE
    "Cyrillic_ZHE_descender":     0x1000496,  # U+0496 CYRILLIC CAPITAL LETTER ZHE WITH DESCENDER
    "Cyrillic_zhe_descender":     0x1000497,  # U+0497 CYRILLIC SMALL LETTER ZHE WITH DESCENDER
    "Cyrillic_KA_descender":      0x100049a,  # U+049A CYRILLIC CAPITAL LETTER KA WITH DESCENDER
    "Cyrillic_ka_descender":      0x100049b,  # U+049B CYRILLIC SMALL LETTER KA WITH DESCENDER
    "Cyrillic_KA_vertstroke":     0x100049c,  # U+049C CYRILLIC CAPITAL LETTER KA WITH VERTICAL STROKE
    "Cyrillic_ka_vertstroke":     0x100049d,  # U+049D CYRILLIC SMALL LETTER KA WITH VERTICAL STROKE
    "Cyrillic_EN_descender":      0x10004a2,  # U+04A2 CYRILLIC CAPITAL LETTER EN WITH DESCENDER
    "Cyrillic_en_descender":      0x10004a3,  # U+04A3 CYRILLIC SMALL LETTER EN WITH DESCENDER
    "Cyrillic_U_straight":        0x10004ae,  # U+04AE CYRILLIC CAPITAL LETTER STRAIGHT U
    "Cyrillic_u_straight":        0x10004af,  # U+04AF CYRILLIC SMALL LETTER STRAIGHT U
    "Cyrillic_U_straight_bar":    0x10004b0,  # U+04B0 CYRILLIC CAPITAL LETTER STRAIGHT U WITH STROKE
    "Cyrillic_u_straight_bar":    0x10004b1,  # U+04B1 CYRILLIC SMALL LETTER STRAIGHT U WITH STROKE
    "Cyrillic_HA_descender":      0x10004b2,  # U+04B2 CYRILLIC CAPITAL LETTER HA WITH DESCENDER
    "Cyrillic_ha_descender":      0x10004b3,  # U+04B3 CYRILLIC SMALL LETTER HA WITH DESCENDER
    "Cyrillic_CHE_descender":     0x10004b6,  # U+04B6 CYRILLIC CAPITAL LETTER CHE WITH DESCENDER
    "Cyrillic_che_descender":     0x10004b7,  # U+04B7 CYRILLIC SMALL LETTER CHE WITH DESCENDER
    "Cyrillic_CHE_vertstroke":    0x10004b8,  # U+04B8 CYRILLIC CAPITAL LETTER CHE WITH VERTICAL STROKE
    "Cyrillic_che_vertstroke":    0x10004b9,  # U+04B9 CYRILLIC SMALL LETTER CHE WITH VERTICAL STROKE
    "Cyrillic_SHHA":              0x10004ba,  # U+04BA CYRILLIC CAPITAL LETTER SHHA
    "Cyrillic_shha":              0x10004bb,  # U+04BB CYRILLIC SMALL LETTER SHHA
    "Cyrillic_SCHWA":             0x10004d8,  # U+04D8 CYRILLIC CAPITAL LETTER SCHWA
    "Cyrillic_schwa":             0x10004d9,  # U+04D9 CYRILLIC SMALL LETTER SCHWA
    "Cyrillic_I_macron":          0x10004e2,  # U+04E2 CYRILLIC CAPITAL LETTER I WITH MACRON
    "Cyrillic_i_macron":          0x10004e3,  # U+04E3 CYRILLIC SMALL LETTER I WITH MACRON
    "Cyrillic_O_bar":             0x10004e8,  # U+04E8 CYRILLIC CAPITAL LETTER BARRED O
    "Cyrillic_o_bar":             0x10004e9,  # U+04E9 CYRILLIC SMALL LETTER BARRED O
    "Cyrillic_U_macron":          0x10004ee,  # U+04EE CYRILLIC CAPITAL LETTER U WITH MACRON
    "Cyrillic_u_macron":          0x10004ef,  # U+04EF CYRILLIC SMALL LETTER U WITH MACRON
    "Serbian_dje":                   0x06a1,  # U+0452 CYRILLIC SMALL LETTER DJE
    "Macedonia_gje":                 0x06a2,  # U+0453 CYRILLIC SMALL LETTER GJE
    "Cyrillic_io":                   0x06a3,  # U+0451 CYRILLIC SMALL LETTER IO
    "Ukrainian_ie":                  0x06a4,  # U+0454 CYRILLIC SMALL LETTER UKRAINIAN IE
    "Macedonia_dse":                 0x06a5,  # U+0455 CYRILLIC SMALL LETTER DZE
    "Ukrainian_i":                   0x06a6,  # U+0456 CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    "Ukrainian_yi":                  0x06a7,  # U+0457 CYRILLIC SMALL LETTER YI
    "Cyrillic_je":                   0x06a8,  # U+0458 CYRILLIC SMALL LETTER JE
    "Cyrillic_lje":                  0x06a9,  # U+0459 CYRILLIC SMALL LETTER LJE
    "Cyrillic_nje":                  0x06aa,  # U+045A CYRILLIC SMALL LETTER NJE
    "Serbian_tshe":                  0x06ab,  # U+045B CYRILLIC SMALL LETTER TSHE
    "Macedonia_kje":                 0x06ac,  # U+045C CYRILLIC SMALL LETTER KJE
    "Ukrainian_ghe_with_upturn":     0x06ad,  # U+0491 CYRILLIC SMALL LETTER GHE WITH UPTURN
    "Byelorussian_shortu":           0x06ae,  # U+045E CYRILLIC SMALL LETTER SHORT U
    "Cyrillic_dzhe":                 0x06af,  # U+045F CYRILLIC SMALL LETTER DZHE
    "numerosign":                    0x06b0,  # U+2116 NUMERO SIGN
    "Serbian_DJE":                   0x06b1,  # U+0402 CYRILLIC CAPITAL LETTER DJE
    "Macedonia_GJE":                 0x06b2,  # U+0403 CYRILLIC CAPITAL LETTER GJE
    "Cyrillic_IO":                   0x06b3,  # U+0401 CYRILLIC CAPITAL LETTER IO
    "Ukrainian_IE":                  0x06b4,  # U+0404 CYRILLIC CAPITAL LETTER UKRAINIAN IE
    "Macedonia_DSE":                 0x06b5,  # U+0405 CYRILLIC CAPITAL LETTER DZE
    "Ukrainian_I":                   0x06b6,  # U+0406 CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    "Ukrainian_YI":                  0x06b7,  # U+0407 CYRILLIC CAPITAL LETTER YI
    "Cyrillic_JE":                   0x06b8,  # U+0408 CYRILLIC CAPITAL LETTER JE
    "Cyrillic_LJE":                  0x06b9,  # U+0409 CYRILLIC CAPITAL LETTER LJE
    "Cyrillic_NJE":                  0x06ba,  # U+040A CYRILLIC CAPITAL LETTER NJE
    "Serbian_TSHE":                  0x06bb,  # U+040B CYRILLIC CAPITAL LETTER TSHE
    "Macedonia_KJE":                 0x06bc,  # U+040C CYRILLIC CAPITAL LETTER KJE
    "Ukrainian_GHE_WITH_UPTURN":     0x06bd,  # U+0490 CYRILLIC CAPITAL LETTER GHE WITH UPTURN
    "Byelorussian_SHORTU":           0x06be,  # U+040E CYRILLIC CAPITAL LETTER SHORT U
    "Cyrillic_DZHE":                 0x06bf,  # U+040F CYRILLIC CAPITAL LETTER DZHE
    "Cyrillic_yu":                   0x06c0,  # U+044E CYRILLIC SMALL LETTER YU
    "Cyrillic_a":                    0x06c1,  # U+0430 CYRILLIC SMALL LETTER A
    "Cyrillic_be":                   0x06c2,  # U+0431 CYRILLIC SMALL LETTER BE
    "Cyrillic_tse":                  0x06c3,  # U+0446 CYRILLIC SMALL LETTER TSE
    "Cyrillic_de":                   0x06c4,  # U+0434 CYRILLIC SMALL LETTER DE
    "Cyrillic_ie":                   0x06c5,  # U+0435 CYRILLIC SMALL LETTER IE
    "Cyrillic_ef":                   0x06c6,  # U+0444 CYRILLIC SMALL LETTER EF
    "Cyrillic_ghe":                  0x06c7,  # U+0433 CYRILLIC SMALL LETTER GHE
    "Cyrillic_ha":                   0x06c8,  # U+0445 CYRILLIC SMALL LETTER HA
    "Cyrillic_i":                    0x06c9,  # U+0438 CYRILLIC SMALL LETTER I
    "Cyrillic_shorti":               0x06ca,  # U+0439 CYRILLIC SMALL LETTER SHORT I
    "Cyrillic_ka":                   0x06cb,  # U+043A CYRILLIC SMALL LETTER KA
    "Cyrillic_el":                   0x06cc,  # U+043B CYRILLIC SMALL LETTER EL
    "Cyrillic_em":                   0x06cd,  # U+043C CYRILLIC SMALL LETTER EM
    "Cyrillic_en":                   0x06ce,  # U+043D CYRILLIC SMALL LETTER EN
    "Cyrillic_o":                    0x06cf,  # U+043E CYRILLIC SMALL LETTER O
    "Cyrillic_pe":                   0x06d0,  # U+043F CYRILLIC SMALL LETTER PE
    "Cyrillic_ya":                   0x06d1,  # U+044F CYRILLIC SMALL LETTER YA
    "Cyrillic_er":                   0x06d2,  # U+0440 CYRILLIC SMALL LETTER ER
    "Cyrillic_es":                   0x06d3,  # U+0441 CYRILLIC SMALL LETTER ES
    "Cyrillic_te":                   0x06d4,  # U+0442 CYRILLIC SMALL LETTER TE
    "Cyrillic_u":                    0x06d5,  # U+0443 CYRILLIC SMALL LETTER U
    "Cyrillic_zhe":                  0x06d6,  # U+0436 CYRILLIC SMALL LETTER ZHE
    "Cyrillic_ve":                   0x06d7,  # U+0432 CYRILLIC SMALL LETTER VE
    "Cyrillic_softsign":             0x06d8,  # U+044C CYRILLIC SMALL LETTER SOFT SIGN
    "Cyrillic_yeru":                 0x06d9,  # U+044B CYRILLIC SMALL LETTER YERU
    "Cyrillic_ze":                   0x06da,  # U+0437 CYRILLIC SMALL LETTER ZE
    "Cyrillic_sha":                  0x06db,  # U+0448 CYRILLIC SMALL LETTER SHA
    "Cyrillic_e":                    0x06dc,  # U+044D CYRILLIC SMALL LETTER E
    "Cyrillic_shcha":                0x06dd,  # U+0449 CYRILLIC SMALL LETTER SHCHA
    "Cyrillic_che":                  0x06de,  # U+0447 CYRILLIC SMALL LETTER CHE
    "Cyrillic_hardsign":             0x06df,  # U+044A CYRILLIC SMALL LETTER HARD SIGN
    "Cyrillic_YU":                   0x06e0,  # U+042E CYRILLIC CAPITAL LETTER YU
    "Cyrillic_A":                    0x06e1,  # U+0410 CYRILLIC CAPITAL LETTER A
    "Cyrillic_BE":                   0x06e2,  # U+0411 CYRILLIC CAPITAL LETTER BE
    "Cyrillic_TSE":                  0x06e3,  # U+0426 CYRILLIC CAPITAL LETTER TSE
    "Cyrillic_DE":                   0x06e4,  # U+0414 CYRILLIC CAPITAL LETTER DE
    "Cyrillic_IE":                   0x06e5,  # U+0415 CYRILLIC CAPITAL LETTER IE
    "Cyrillic_EF":                   0x06e6,  # U+0424 CYRILLIC CAPITAL LETTER EF
    "Cyrillic_GHE":                  0x06e7,  # U+0413 CYRILLIC CAPITAL LETTER GHE
    "Cyrillic_HA":                   0x06e8,  # U+0425 CYRILLIC CAPITAL LETTER HA
    "Cyrillic_I":                    0x06e9,  # U+0418 CYRILLIC CAPITAL LETTER I
    "Cyrillic_SHORTI":               0x06ea,  # U+0419 CYRILLIC CAPITAL LETTER SHORT I
    "Cyrillic_KA":                   0x06eb,  # U+041A CYRILLIC CAPITAL LETTER KA
    "Cyrillic_EL":                   0x06ec,  # U+041B CYRILLIC CAPITAL LETTER EL
    "Cyrillic_EM":                   0x06ed,  # U+041C CYRILLIC CAPITAL LETTER EM
    "Cyrillic_EN":                   0x06ee,  # U+041D CYRILLIC CAPITAL LETTER EN
    "Cyrillic_O":                    0x06ef,  # U+041E CYRILLIC CAPITAL LETTER O
    "Cyrillic_PE":                   0x06f0,  # U+041F CYRILLIC CAPITAL LETTER PE
    "Cyrillic_YA":                   0x06f1,  # U+042F CYRILLIC CAPITAL LETTER YA
    "Cyrillic_ER":                   0x06f2,  # U+0420 CYRILLIC CAPITAL LETTER ER
    "Cyrillic_ES":                   0x06f3,  # U+0421 CYRILLIC CAPITAL LETTER ES
    "Cyrillic_TE":                   0x06f4,  # U+0422 CYRILLIC CAPITAL LETTER TE
    "Cyrillic_U":                    0x06f5,  # U+0423 CYRILLIC CAPITAL LETTER U
    "Cyrillic_ZHE":                  0x06f6,  # U+0416 CYRILLIC CAPITAL LETTER ZHE
    "Cyrillic_VE":                   0x06f7,  # U+0412 CYRILLIC CAPITAL LETTER VE
    "Cyrillic_SOFTSIGN":             0x06f8,  # U+042C CYRILLIC CAPITAL LETTER SOFT SIGN
    "Cyrillic_YERU":                 0x06f9,  # U+042B CYRILLIC CAPITAL LETTER YERU
    "Cyrillic_ZE":                   0x06fa,  # U+0417 CYRILLIC CAPITAL LETTER ZE
    "Cyrillic_SHA":                  0x06fb,  # U+0428 CYRILLIC CAPITAL LETTER SHA
    "Cyrillic_E":                    0x06fc,  # U+042D CYRILLIC CAPITAL LETTER E
    "Cyrillic_SHCHA":                0x06fd,  # U+0429 CYRILLIC CAPITAL LETTER SHCHA
    "Cyrillic_CHE":                  0x06fe,  # U+0427 CYRILLIC CAPITAL LETTER CHE
    "Cyrillic_HARDSIGN":             0x06ff,  # U+042A CYRILLIC CAPITAL LETTER HARD SIGN
    "Greek_ALPHAaccent":             0x07a1,  # U+0386 GREEK CAPITAL LETTER ALPHA WITH TONOS
    "Greek_EPSILONaccent":           0x07a2,  # U+0388 GREEK CAPITAL LETTER EPSILON WITH TONOS
    "Greek_ETAaccent":               0x07a3,  # U+0389 GREEK CAPITAL LETTER ETA WITH TONOS
    "Greek_IOTAaccent":              0x07a4,  # U+038A GREEK CAPITAL LETTER IOTA WITH TONOS
    "Greek_IOTAdieresis":            0x07a5,  # U+03AA GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
    "Greek_IOTAdiaeresis":           0x07a5,  # old typo
    "Greek_OMICRONaccent":           0x07a7,  # U+038C GREEK CAPITAL LETTER OMICRON WITH TONOS
    "Greek_UPSILONaccent":           0x07a8,  # U+038E GREEK CAPITAL LETTER UPSILON WITH TONOS
    "Greek_UPSILONdieresis":         0x07a9,  # U+03AB GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
    "Greek_OMEGAaccent":             0x07ab,  # U+038F GREEK CAPITAL LETTER OMEGA WITH TONOS
    "Greek_accentdieresis":          0x07ae,  # U+0385 GREEK DIALYTIKA TONOS
    "Greek_horizbar":                0x07af,  # U+2015 HORIZONTAL BAR
    "Greek_alphaaccent":             0x07b1,  # U+03AC GREEK SMALL LETTER ALPHA WITH TONOS
    "Greek_epsilonaccent":           0x07b2,  # U+03AD GREEK SMALL LETTER EPSILON WITH TONOS
    "Greek_etaaccent":               0x07b3,  # U+03AE GREEK SMALL LETTER ETA WITH TONOS
    "Greek_iotaaccent":              0x07b4,  # U+03AF GREEK SMALL LETTER IOTA WITH TONOS
    "Greek_iotadieresis":            0x07b5,  # U+03CA GREEK SMALL LETTER IOTA WITH DIALYTIKA
    "Greek_iotaaccentdieresis":      0x07b6,  # U+0390 GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
    "Greek_omicronaccent":           0x07b7,  # U+03CC GREEK SMALL LETTER OMICRON WITH TONOS
    "Greek_upsilonaccent":           0x07b8,  # U+03CD GREEK SMALL LETTER UPSILON WITH TONOS
    "Greek_upsilondieresis":         0x07b9,  # U+03CB GREEK SMALL LETTER UPSILON WITH DIALYTIKA
    "Greek_upsilonaccentdieresis":   0x07ba,  # U+03B0 GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
    "Greek_omegaaccent":             0x07bb,  # U+03CE GREEK SMALL LETTER OMEGA WITH TONOS
    "Greek_ALPHA":                   0x07c1,  # U+0391 GREEK CAPITAL LETTER ALPHA
    "Greek_BETA":                    0x07c2,  # U+0392 GREEK CAPITAL LETTER BETA
    "Greek_GAMMA":                   0x07c3,  # U+0393 GREEK CAPITAL LETTER GAMMA
    "Greek_DELTA":                   0x07c4,  # U+0394 GREEK CAPITAL LETTER DELTA
    "Greek_EPSILON":                 0x07c5,  # U+0395 GREEK CAPITAL LETTER EPSILON
    "Greek_ZETA":                    0x07c6,  # U+0396 GREEK CAPITAL LETTER ZETA
    "Greek_ETA":                     0x07c7,  # U+0397 GREEK CAPITAL LETTER ETA
    "Greek_THETA":                   0x07c8,  # U+0398 GREEK CAPITAL LETTER THETA
    "Greek_IOTA":                    0x07c9,  # U+0399 GREEK CAPITAL LETTER IOTA
    "Greek_KAPPA":                   0x07ca,  # U+039A GREEK CAPITAL LETTER KAPPA
    "Greek_LAMDA":                   0x07cb,  # U+039B GREEK CAPITAL LETTER LAMDA
    "Greek_LAMBDA":                  0x07cb,  # U+039B GREEK CAPITAL LETTER LAMDA
    "Greek_MU":                      0x07cc,  # U+039C GREEK CAPITAL LETTER MU
    "Greek_NU":                      0x07cd,  # U+039D GREEK CAPITAL LETTER NU
    "Greek_XI":                      0x07ce,  # U+039E GREEK CAPITAL LETTER XI
    "Greek_OMICRON":                 0x07cf,  # U+039F GREEK CAPITAL LETTER OMICRON
    "Greek_PI":                      0x07d0,  # U+03A0 GREEK CAPITAL LETTER PI
    "Greek_RHO":                     0x07d1,  # U+03A1 GREEK CAPITAL LETTER RHO
    "Greek_SIGMA":                   0x07d2,  # U+03A3 GREEK CAPITAL LETTER SIGMA
    "Greek_TAU":                     0x07d4,  # U+03A4 GREEK CAPITAL LETTER TAU
    "Greek_UPSILON":                 0x07d5,  # U+03A5 GREEK CAPITAL LETTER UPSILON
    "Greek_PHI":                     0x07d6,  # U+03A6 GREEK CAPITAL LETTER PHI
    "Greek_CHI":                     0x07d7,  # U+03A7 GREEK CAPITAL LETTER CHI
    "Greek_PSI":                     0x07d8,  # U+03A8 GREEK CAPITAL LETTER PSI
    "Greek_OMEGA":                   0x07d9,  # U+03A9 GREEK CAPITAL LETTER OMEGA
    "Greek_alpha":                   0x07e1,  # U+03B1 GREEK SMALL LETTER ALPHA
    "Greek_beta":                    0x07e2,  # U+03B2 GREEK SMALL LETTER BETA
    "Greek_gamma":                   0x07e3,  # U+03B3 GREEK SMALL LETTER GAMMA
    "Greek_delta":                   0x07e4,  # U+03B4 GREEK SMALL LETTER DELTA
    "Greek_epsilon":                 0x07e5,  # U+03B5 GREEK SMALL LETTER EPSILON
    "Greek_zeta":                    0x07e6,  # U+03B6 GREEK SMALL LETTER ZETA
    "Greek_eta":                     0x07e7,  # U+03B7 GREEK SMALL LETTER ETA
    "Greek_theta":                   0x07e8,  # U+03B8 GREEK SMALL LETTER THETA
    "Greek_iota":                    0x07e9,  # U+03B9 GREEK SMALL LETTER IOTA
    "Greek_kappa":                   0x07ea,  # U+03BA GREEK SMALL LETTER KAPPA
    "Greek_lamda":                   0x07eb,  # U+03BB GREEK SMALL LETTER LAMDA
    "Greek_lambda":                  0x07eb,  # U+03BB GREEK SMALL LETTER LAMDA
    "Greek_mu":                      0x07ec,  # U+03BC GREEK SMALL LETTER MU
    "Greek_nu":                      0x07ed,  # U+03BD GREEK SMALL LETTER NU
    "Greek_xi":                      0x07ee,  # U+03BE GREEK SMALL LETTER XI
    "Greek_omicron":                 0x07ef,  # U+03BF GREEK SMALL LETTER OMICRON
    "Greek_pi":                      0x07f0,  # U+03C0 GREEK SMALL LETTER PI
    "Greek_rho":                     0x07f1,  # U+03C1 GREEK SMALL LETTER RHO
    "Greek_sigma":                   0x07f2,  # U+03C3 GREEK SMALL LETTER SIGMA
    "Greek_finalsmallsigma":         0x07f3,  # U+03C2 GREEK SMALL LETTER FINAL SIGMA
    "Greek_tau":                     0x07f4,  # U+03C4 GREEK SMALL LETTER TAU
    "Greek_upsilon":                 0x07f5,  # U+03C5 GREEK SMALL LETTER UPSILON
    "Greek_phi":                     0x07f6,  # U+03C6 GREEK SMALL LETTER PHI
    "Greek_chi":                     0x07f7,  # U+03C7 GREEK SMALL LETTER CHI
    "Greek_psi":                     0x07f8,  # U+03C8 GREEK SMALL LETTER PSI
    "Greek_omega":                   0x07f9,  # U+03C9 GREEK SMALL LETTER OMEGA
    "Greek_switch":                  0xff7e,  # Alias for mode_switch
    "leftradical":                   0x08a1,  # U+23B7 RADICAL SYMBOL BOTTOM
    "topleftradical":                0x08a2,  #(U+250C BOX DRAWINGS LIGHT DOWN AND RIGHT)
    "horizconnector":                0x08a3,  #(U+2500 BOX DRAWINGS LIGHT HORIZONTAL)
    "topintegral":                   0x08a4,  # U+2320 TOP HALF INTEGRAL
    "botintegral":                   0x08a5,  # U+2321 BOTTOM HALF INTEGRAL
    "vertconnector":                 0x08a6,  #(U+2502 BOX DRAWINGS LIGHT VERTICAL)
    "topleftsqbracket":              0x08a7,  # U+23A1 LEFT SQUARE BRACKET UPPER CORNER
    "botleftsqbracket":              0x08a8,  # U+23A3 LEFT SQUARE BRACKET LOWER CORNER
    "toprightsqbracket":             0x08a9,  # U+23A4 RIGHT SQUARE BRACKET UPPER CORNER
    "botrightsqbracket":             0x08aa,  # U+23A6 RIGHT SQUARE BRACKET LOWER CORNER
    "topleftparens":                 0x08ab,  # U+239B LEFT PARENTHESIS UPPER HOOK
    "botleftparens":                 0x08ac,  # U+239D LEFT PARENTHESIS LOWER HOOK
    "toprightparens":                0x08ad,  # U+239E RIGHT PARENTHESIS UPPER HOOK
    "botrightparens":                0x08ae,  # U+23A0 RIGHT PARENTHESIS LOWER HOOK
    "leftmiddlecurlybrace":          0x08af,  # U+23A8 LEFT CURLY BRACKET MIDDLE PIECE
    "rightmiddlecurlybrace":         0x08b0,  # U+23AC RIGHT CURLY BRACKET MIDDLE PIECE
    "topleftsummation":              0x08b1,
    "botleftsummation":              0x08b2,
    "topvertsummationconnector":     0x08b3,
    "botvertsummationconnector":     0x08b4,
    "toprightsummation":             0x08b5,
    "botrightsummation":             0x08b6,
    "rightmiddlesummation":          0x08b7,
    "lessthanequal":                 0x08bc,  # U+2264 LESS-THAN OR EQUAL TO
    "notequal":                      0x08bd,  # U+2260 NOT EQUAL TO
    "greaterthanequal":              0x08be,  # U+2265 GREATER-THAN OR EQUAL TO
    "integral":                      0x08bf,  # U+222B INTEGRAL
    "therefore":                     0x08c0,  # U+2234 THEREFORE
    "variation":                     0x08c1,  # U+221D PROPORTIONAL TO
    "infinity":                      0x08c2,  # U+221E INFINITY
    "nabla":                         0x08c5,  # U+2207 NABLA
    "approximate":                   0x08c8,  # U+223C TILDE OPERATOR
    "similarequal":                  0x08c9,  # U+2243 ASYMPTOTICALLY EQUAL TO
    "ifonlyif":                      0x08cd,  # U+21D4 LEFT RIGHT DOUBLE ARROW
    "implies":                       0x08ce,  # U+21D2 RIGHTWARDS DOUBLE ARROW
    "identical":                     0x08cf,  # U+2261 IDENTICAL TO
    "radical":                       0x08d6,  # U+221A SQUARE ROOT
    "includedin":                    0x08da,  # U+2282 SUBSET OF
    "includes":                      0x08db,  # U+2283 SUPERSET OF
    "intersection":                  0x08dc,  # U+2229 INTERSECTION
    "union":                         0x08dd,  # U+222A UNION
    "logicaland":                    0x08de,  # U+2227 LOGICAL AND
    "logicalor":                     0x08df,  # U+2228 LOGICAL OR
    "partialderivative":             0x08ef,  # U+2202 PARTIAL DIFFERENTIAL
    "function":                      0x08f6,  # U+0192 LATIN SMALL LETTER F WITH HOOK
    "leftarrow":                     0x08fb,  # U+2190 LEFTWARDS ARROW
    "uparrow":                       0x08fc,  # U+2191 UPWARDS ARROW
    "rightarrow":                    0x08fd,  # U+2192 RIGHTWARDS ARROW
    "downarrow":                     0x08fe,  # U+2193 DOWNWARDS ARROW
    "blank":                         0x09df,
    "soliddiamond":                  0x09e0,  # U+25C6 BLACK DIAMOND
    "checkerboard":                  0x09e1,  # U+2592 MEDIUM SHADE
    "ht":                            0x09e2,  # U+2409 SYMBOL FOR HORIZONTAL TABULATION
    "ff":                            0x09e3,  # U+240C SYMBOL FOR FORM FEED
    "cr":                            0x09e4,  # U+240D SYMBOL FOR CARRIAGE RETURN
    "lf":                            0x09e5,  # U+240A SYMBOL FOR LINE FEED
    "nl":                            0x09e8,  # U+2424 SYMBOL FOR NEWLINE
    "vt":                            0x09e9,  # U+240B SYMBOL FOR VERTICAL TABULATION
    "lowrightcorner":                0x09ea,  # U+2518 BOX DRAWINGS LIGHT UP AND LEFT
    "uprightcorner":                 0x09eb,  # U+2510 BOX DRAWINGS LIGHT DOWN AND LEFT
    "upleftcorner":                  0x09ec,  # U+250C BOX DRAWINGS LIGHT DOWN AND RIGHT
    "lowleftcorner":                 0x09ed,  # U+2514 BOX DRAWINGS LIGHT UP AND RIGHT
    "crossinglines":                 0x09ee,  # U+253C BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    "horizlinescan1":                0x09ef,  # U+23BA HORIZONTAL SCAN LINE-1
    "horizlinescan3":                0x09f0,  # U+23BB HORIZONTAL SCAN LINE-3
    "horizlinescan5":                0x09f1,  # U+2500 BOX DRAWINGS LIGHT HORIZONTAL
    "horizlinescan7":                0x09f2,  # U+23BC HORIZONTAL SCAN LINE-7
    "horizlinescan9":                0x09f3,  # U+23BD HORIZONTAL SCAN LINE-9
    "leftt":                         0x09f4,  # U+251C BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    "rightt":                        0x09f5,  # U+2524 BOX DRAWINGS LIGHT VERTICAL AND LEFT
    "bott":                          0x09f6,  # U+2534 BOX DRAWINGS LIGHT UP AND HORIZONTAL
    "topt":                          0x09f7,  # U+252C BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    "vertbar":                       0x09f8,  # U+2502 BOX DRAWINGS LIGHT VERTICAL
    "emspace":                       0x0aa1,  # U+2003 EM SPACE
    "enspace":                       0x0aa2,  # U+2002 EN SPACE
    "em3space":                      0x0aa3,  # U+2004 THREE-PER-EM SPACE
    "em4space":                      0x0aa4,  # U+2005 FOUR-PER-EM SPACE
    "digitspace":                    0x0aa5,  # U+2007 FIGURE SPACE
    "punctspace":                    0x0aa6,  # U+2008 PUNCTUATION SPACE
    "thinspace":                     0x0aa7,  # U+2009 THIN SPACE
    "hairspace":                     0x0aa8,  # U+200A HAIR SPACE
    "emdash":                        0x0aa9,  # U+2014 EM DASH
    "endash":                        0x0aaa,  # U+2013 EN DASH
    "signifblank":                   0x0aac,  #(U+2423 OPEN BOX)
    "ellipsis":                      0x0aae,  # U+2026 HORIZONTAL ELLIPSIS
    "doubbaselinedot":               0x0aaf,  # U+2025 TWO DOT LEADER
    "onethird":                      0x0ab0,  # U+2153 VULGAR FRACTION ONE THIRD
    "twothirds":                     0x0ab1,  # U+2154 VULGAR FRACTION TWO THIRDS
    "onefifth":                      0x0ab2,  # U+2155 VULGAR FRACTION ONE FIFTH
    "twofifths":                     0x0ab3,  # U+2156 VULGAR FRACTION TWO FIFTHS
    "threefifths":                   0x0ab4,  # U+2157 VULGAR FRACTION THREE FIFTHS
    "fourfifths":                    0x0ab5,  # U+2158 VULGAR FRACTION FOUR FIFTHS
    "onesixth":                      0x0ab6,  # U+2159 VULGAR FRACTION ONE SIXTH
    "fivesixths":                    0x0ab7,  # U+215A VULGAR FRACTION FIVE SIXTHS
    "careof":                        0x0ab8,  # U+2105 CARE OF
    "figdash":                       0x0abb,  # U+2012 FIGURE DASH
    "leftanglebracket":              0x0abc,  #(U+2329 LEFT-POINTING ANGLE BRACKET)
    "decimalpoint":                  0x0abd,  #(U+002E FULL STOP)
    "rightanglebracket":             0x0abe,  #(U+232A RIGHT-POINTING ANGLE BRACKET)
    "marker":                        0x0abf,
    "oneeighth":                     0x0ac3,  # U+215B VULGAR FRACTION ONE EIGHTH
    "threeeighths":                  0x0ac4,  # U+215C VULGAR FRACTION THREE EIGHTHS
    "fiveeighths":                   0x0ac5,  # U+215D VULGAR FRACTION FIVE EIGHTHS
    "seveneighths":                  0x0ac6,  # U+215E VULGAR FRACTION SEVEN EIGHTHS
    "trademark":                     0x0ac9,  # U+2122 TRADE MARK SIGN
    "signaturemark":                 0x0aca,  #(U+2613 SALTIRE)
    "trademarkincircle":             0x0acb,
    "leftopentriangle":              0x0acc,  #(U+25C1 WHITE LEFT-POINTING TRIANGLE)
    "rightopentriangle":             0x0acd,  #(U+25B7 WHITE RIGHT-POINTING TRIANGLE)
    "emopencircle":                  0x0ace,  #(U+25CB WHITE CIRCLE)
    "emopenrectangle":               0x0acf,  #(U+25AF WHITE VERTICAL RECTANGLE)
    "leftsinglequotemark":           0x0ad0,  # U+2018 LEFT SINGLE QUOTATION MARK
    "rightsinglequotemark":          0x0ad1,  # U+2019 RIGHT SINGLE QUOTATION MARK
    "leftdoublequotemark":           0x0ad2,  # U+201C LEFT DOUBLE QUOTATION MARK
    "rightdoublequotemark":          0x0ad3,  # U+201D RIGHT DOUBLE QUOTATION MARK
    "prescription":                  0x0ad4,  # U+211E PRESCRIPTION TAKE
    "permille":                      0x0ad5,  # U+2030 PER MILLE SIGN
    "minutes":                       0x0ad6,  # U+2032 PRIME
    "seconds":                       0x0ad7,  # U+2033 DOUBLE PRIME
    "latincross":                    0x0ad9,  # U+271D LATIN CROSS
    "hexagram":                      0x0ada,
    "filledrectbullet":              0x0adb,  #(U+25AC BLACK RECTANGLE)
    "filledlefttribullet":           0x0adc,  #(U+25C0 BLACK LEFT-POINTING TRIANGLE)
    "filledrighttribullet":          0x0add,  #(U+25B6 BLACK RIGHT-POINTING TRIANGLE)
    "emfilledcircle":                0x0ade,  #(U+25CF BLACK CIRCLE)
    "emfilledrect":                  0x0adf,  #(U+25AE BLACK VERTICAL RECTANGLE)
    "enopencircbullet":              0x0ae0,  #(U+25E6 WHITE BULLET)
    "enopensquarebullet":            0x0ae1,  #(U+25AB WHITE SMALL SQUARE)
    "openrectbullet":                0x0ae2,  #(U+25AD WHITE RECTANGLE)
    "opentribulletup":               0x0ae3,  #(U+25B3 WHITE UP-POINTING TRIANGLE)
    "opentribulletdown":             0x0ae4,  #(U+25BD WHITE DOWN-POINTING TRIANGLE)
    "openstar":                      0x0ae5,  #(U+2606 WHITE STAR)
    "enfilledcircbullet":            0x0ae6,  #(U+2022 BULLET)
    "enfilledsqbullet":              0x0ae7,  #(U+25AA BLACK SMALL SQUARE)
    "filledtribulletup":             0x0ae8,  #(U+25B2 BLACK UP-POINTING TRIANGLE)
    "filledtribulletdown":           0x0ae9,  #(U+25BC BLACK DOWN-POINTING TRIANGLE)
    "leftpointer":                   0x0aea,  #(U+261C WHITE LEFT POINTING INDEX)
    "rightpointer":                  0x0aeb,  #(U+261E WHITE RIGHT POINTING INDEX)
    "club":                          0x0aec,  # U+2663 BLACK CLUB SUIT
    "diamond":                       0x0aed,  # U+2666 BLACK DIAMOND SUIT
    "heart":                         0x0aee,  # U+2665 BLACK HEART SUIT
    "maltesecross":                  0x0af0,  # U+2720 MALTESE CROSS
    "dagger":                        0x0af1,  # U+2020 DAGGER
    "doubledagger":                  0x0af2,  # U+2021 DOUBLE DAGGER
    "checkmark":                     0x0af3,  # U+2713 CHECK MARK
    "ballotcross":                   0x0af4,  # U+2717 BALLOT X
    "musicalsharp":                  0x0af5,  # U+266F MUSIC SHARP SIGN
    "musicalflat":                   0x0af6,  # U+266D MUSIC FLAT SIGN
    "malesymbol":                    0x0af7,  # U+2642 MALE SIGN
    "femalesymbol":                  0x0af8,  # U+2640 FEMALE SIGN
    "telephone":                     0x0af9,  # U+260E BLACK TELEPHONE
    "telephonerecorder":             0x0afa,  # U+2315 TELEPHONE RECORDER
    "phonographcopyright":           0x0afb,  # U+2117 SOUND RECORDING COPYRIGHT
    "caret":                         0x0afc,  # U+2038 CARET
    "singlelowquotemark":            0x0afd,  # U+201A SINGLE LOW-9 QUOTATION MARK
    "doublelowquotemark":            0x0afe,  # U+201E DOUBLE LOW-9 QUOTATION MARK
    "cursor":                        0x0aff,
    "leftcaret":                     0x0ba3,  #(U+003C LESS-THAN SIGN)
    "rightcaret":                    0x0ba6,  #(U+003E GREATER-THAN SIGN)
    "downcaret":                     0x0ba8,  #(U+2228 LOGICAL OR)
    "upcaret":                       0x0ba9,  #(U+2227 LOGICAL AND)
    "overbar":                       0x0bc0,  #(U+00AF MACRON)
    "downtack":                      0x0bc2,  # U+22A4 DOWN TACK
    "upshoe":                        0x0bc3,  #(U+2229 INTERSECTION)
    "downstile":                     0x0bc4,  # U+230A LEFT FLOOR
    "underbar":                      0x0bc6,  #(U+005F LOW LINE)
    "jot":                           0x0bca,  # U+2218 RING OPERATOR
    "quad":                          0x0bcc,  # U+2395 APL FUNCTIONAL SYMBOL QUAD
    "uptack":                        0x0bce,  # U+22A5 UP TACK
    "circle":                        0x0bcf,  # U+25CB WHITE CIRCLE
    "upstile":                       0x0bd3,  # U+2308 LEFT CEILING
    "downshoe":                      0x0bd6,  #(U+222A UNION)
    "rightshoe":                     0x0bd8,  #(U+2283 SUPERSET OF)
    "leftshoe":                      0x0bda,  #(U+2282 SUBSET OF)
    "lefttack":                      0x0bdc,  # U+22A3 LEFT TACK
    "righttack":                     0x0bfc,  # U+22A2 RIGHT TACK
    "hebrew_doublelowline":          0x0cdf,  # U+2017 DOUBLE LOW LINE
    "hebrew_aleph":                  0x0ce0,  # U+05D0 HEBREW LETTER ALEF
    "hebrew_bet":                    0x0ce1,  # U+05D1 HEBREW LETTER BET
    "hebrew_gimel":                  0x0ce2,  # U+05D2 HEBREW LETTER GIMEL
    "hebrew_dalet":                  0x0ce3,  # U+05D3 HEBREW LETTER DALET
    "hebrew_he":                     0x0ce4,  # U+05D4 HEBREW LETTER HE
    "hebrew_waw":                    0x0ce5,  # U+05D5 HEBREW LETTER VAV
    "hebrew_zain":                   0x0ce6,  # U+05D6 HEBREW LETTER ZAYIN
    "hebrew_chet":                   0x0ce7,  # U+05D7 HEBREW LETTER HET
    "hebrew_tet":                    0x0ce8,  # U+05D8 HEBREW LETTER TET
    "hebrew_yod":                    0x0ce9,  # U+05D9 HEBREW LETTER YOD
    "hebrew_finalkaph":              0x0cea,  # U+05DA HEBREW LETTER FINAL KAF
    "hebrew_kaph":                   0x0ceb,  # U+05DB HEBREW LETTER KAF
    "hebrew_lamed":                  0x0cec,  # U+05DC HEBREW LETTER LAMED
    "hebrew_finalmem":               0x0ced,  # U+05DD HEBREW LETTER FINAL MEM
    "hebrew_mem":                    0x0cee,  # U+05DE HEBREW LETTER MEM
    "hebrew_finalnun":               0x0cef,  # U+05DF HEBREW LETTER FINAL NUN
    "hebrew_nun":                    0x0cf0,  # U+05E0 HEBREW LETTER NUN
    "hebrew_samech":                 0x0cf1,  # U+05E1 HEBREW LETTER SAMEKH
    "hebrew_ayin":                   0x0cf2,  # U+05E2 HEBREW LETTER AYIN
    "hebrew_finalpe":                0x0cf3,  # U+05E3 HEBREW LETTER FINAL PE
    "hebrew_pe":                     0x0cf4,  # U+05E4 HEBREW LETTER PE
    "hebrew_finalzade":              0x0cf5,  # U+05E5 HEBREW LETTER FINAL TSADI
    "hebrew_zade":                   0x0cf6,  # U+05E6 HEBREW LETTER TSADI
    "hebrew_qoph":                   0x0cf7,  # U+05E7 HEBREW LETTER QOF
    "hebrew_resh":                   0x0cf8,  # U+05E8 HEBREW LETTER RESH
    "hebrew_shin":                   0x0cf9,  # U+05E9 HEBREW LETTER SHIN
    "hebrew_taw":                    0x0cfa,  # U+05EA HEBREW LETTER TAV
    "Hebrew_switch":                 0xff7e,  # Alias for mode_switch
    "Thai_kokai":                    0x0da1,  # U+0E01 THAI CHARACTER KO KAI
    "Thai_khokhai":                  0x0da2,  # U+0E02 THAI CHARACTER KHO KHAI
    "Thai_khokhuat":                 0x0da3,  # U+0E03 THAI CHARACTER KHO KHUAT
    "Thai_khokhwai":                 0x0da4,  # U+0E04 THAI CHARACTER KHO KHWAI
    "Thai_khokhon":                  0x0da5,  # U+0E05 THAI CHARACTER KHO KHON
    "Thai_khorakhang":               0x0da6,  # U+0E06 THAI CHARACTER KHO RAKHANG
    "Thai_ngongu":                   0x0da7,  # U+0E07 THAI CHARACTER NGO NGU
    "Thai_chochan":                  0x0da8,  # U+0E08 THAI CHARACTER CHO CHAN
    "Thai_choching":                 0x0da9,  # U+0E09 THAI CHARACTER CHO CHING
    "Thai_chochang":                 0x0daa,  # U+0E0A THAI CHARACTER CHO CHANG
    "Thai_soso":                     0x0dab,  # U+0E0B THAI CHARACTER SO SO
    "Thai_chochoe":                  0x0dac,  # U+0E0C THAI CHARACTER CHO CHOE
    "Thai_yoying":                   0x0dad,  # U+0E0D THAI CHARACTER YO YING
    "Thai_dochada":                  0x0dae,  # U+0E0E THAI CHARACTER DO CHADA
    "Thai_topatak":                  0x0daf,  # U+0E0F THAI CHARACTER TO PATAK
    "Thai_thothan":                  0x0db0,  # U+0E10 THAI CHARACTER THO THAN
    "Thai_thonangmontho":            0x0db1,  # U+0E11 THAI CHARACTER THO NANGMONTHO
    "Thai_thophuthao":               0x0db2,  # U+0E12 THAI CHARACTER THO PHUTHAO
    "Thai_nonen":                    0x0db3,  # U+0E13 THAI CHARACTER NO NEN
    "Thai_dodek":                    0x0db4,  # U+0E14 THAI CHARACTER DO DEK
    "Thai_totao":                    0x0db5,  # U+0E15 THAI CHARACTER TO TAO
    "Thai_thothung":                 0x0db6,  # U+0E16 THAI CHARACTER THO THUNG
    "Thai_thothahan":                0x0db7,  # U+0E17 THAI CHARACTER THO THAHAN
    "Thai_thothong":                 0x0db8,  # U+0E18 THAI CHARACTER THO THONG
    "Thai_nonu":                     0x0db9,  # U+0E19 THAI CHARACTER NO NU
    "Thai_bobaimai":                 0x0dba,  # U+0E1A THAI CHARACTER BO BAIMAI
    "Thai_popla":                    0x0dbb,  # U+0E1B THAI CHARACTER PO PLA
    "Thai_phophung":                 0x0dbc,  # U+0E1C THAI CHARACTER PHO PHUNG
    "Thai_fofa":                     0x0dbd,  # U+0E1D THAI CHARACTER FO FA
    "Thai_phophan":                  0x0dbe,  # U+0E1E THAI CHARACTER PHO PHAN
    "Thai_fofan":                    0x0dbf,  # U+0E1F THAI CHARACTER FO FAN
    "Thai_phosamphao":               0x0dc0,  # U+0E20 THAI CHARACTER PHO SAMPHAO
    "Thai_moma":                     0x0dc1,  # U+0E21 THAI CHARACTER MO MA
    "Thai_yoyak":                    0x0dc2,  # U+0E22 THAI CHARACTER YO YAK
    "Thai_rorua":                    0x0dc3,  # U+0E23 THAI CHARACTER RO RUA
    "Thai_ru":                       0x0dc4,  # U+0E24 THAI CHARACTER RU
    "Thai_loling":                   0x0dc5,  # U+0E25 THAI CHARACTER LO LING
    "Thai_lu":                       0x0dc6,  # U+0E26 THAI CHARACTER LU
    "Thai_wowaen":                   0x0dc7,  # U+0E27 THAI CHARACTER WO WAEN
    "Thai_sosala":                   0x0dc8,  # U+0E28 THAI CHARACTER SO SALA
    "Thai_sorusi":                   0x0dc9,  # U+0E29 THAI CHARACTER SO RUSI
    "Thai_sosua":                    0x0dca,  # U+0E2A THAI CHARACTER SO SUA
    "Thai_hohip":                    0x0dcb,  # U+0E2B THAI CHARACTER HO HIP
    "Thai_lochula":                  0x0dcc,  # U+0E2C THAI CHARACTER LO CHULA
    "Thai_oang":                     0x0dcd,  # U+0E2D THAI CHARACTER O ANG
    "Thai_honokhuk":                 0x0dce,  # U+0E2E THAI CHARACTER HO NOKHUK
    "Thai_paiyannoi":                0x0dcf,  # U+0E2F THAI CHARACTER PAIYANNOI
    "Thai_saraa":                    0x0dd0,  # U+0E30 THAI CHARACTER SARA A
    "Thai_maihanakat":               0x0dd1,  # U+0E31 THAI CHARACTER MAI HAN-AKAT
    "Thai_saraaa":                   0x0dd2,  # U+0E32 THAI CHARACTER SARA AA
    "Thai_saraam":                   0x0dd3,  # U+0E33 THAI CHARACTER SARA AM
    "Thai_sarai":                    0x0dd4,  # U+0E34 THAI CHARACTER SARA I
    "Thai_saraii":                   0x0dd5,  # U+0E35 THAI CHARACTER SARA II
    "Thai_saraue":                   0x0dd6,  # U+0E36 THAI CHARACTER SARA UE
    "Thai_sarauee":                  0x0dd7,  # U+0E37 THAI CHARACTER SARA UEE
    "Thai_sarau":                    0x0dd8,  # U+0E38 THAI CHARACTER SARA U
    "Thai_sarauu":                   0x0dd9,  # U+0E39 THAI CHARACTER SARA UU
    "Thai_phinthu":                  0x0dda,  # U+0E3A THAI CHARACTER PHINTHU
    "Thai_maihanakat_maitho":        0x0dde,
    "Thai_baht":                     0x0ddf,  # U+0E3F THAI CURRENCY SYMBOL BAHT
    "Thai_sarae":                    0x0de0,  # U+0E40 THAI CHARACTER SARA E
    "Thai_saraae":                   0x0de1,  # U+0E41 THAI CHARACTER SARA AE
    "Thai_sarao":                    0x0de2,  # U+0E42 THAI CHARACTER SARA O
    "Thai_saraaimaimuan":            0x0de3,  # U+0E43 THAI CHARACTER SARA AI MAIMUAN
    "Thai_saraaimaimalai":           0x0de4,  # U+0E44 THAI CHARACTER SARA AI MAIMALAI
    "Thai_lakkhangyao":              0x0de5,  # U+0E45 THAI CHARACTER LAKKHANGYAO
    "Thai_maiyamok":                 0x0de6,  # U+0E46 THAI CHARACTER MAIYAMOK
    "Thai_maitaikhu":                0x0de7,  # U+0E47 THAI CHARACTER MAITAIKHU
    "Thai_maiek":                    0x0de8,  # U+0E48 THAI CHARACTER MAI EK
    "Thai_maitho":                   0x0de9,  # U+0E49 THAI CHARACTER MAI THO
    "Thai_maitri":                   0x0dea,  # U+0E4A THAI CHARACTER MAI TRI
    "Thai_maichattawa":              0x0deb,  # U+0E4B THAI CHARACTER MAI CHATTAWA
    "Thai_thanthakhat":              0x0dec,  # U+0E4C THAI CHARACTER THANTHAKHAT
    "Thai_nikhahit":                 0x0ded,  # U+0E4D THAI CHARACTER NIKHAHIT
    "Thai_leksun":                   0x0df0,  # U+0E50 THAI DIGIT ZERO
    "Thai_leknung":                  0x0df1,  # U+0E51 THAI DIGIT ONE
    "Thai_leksong":                  0x0df2,  # U+0E52 THAI DIGIT TWO
    "Thai_leksam":                   0x0df3,  # U+0E53 THAI DIGIT THREE
    "Thai_leksi":                    0x0df4,  # U+0E54 THAI DIGIT FOUR
    "Thai_lekha":                    0x0df5,  # U+0E55 THAI DIGIT FIVE
    "Thai_lekhok":                   0x0df6,  # U+0E56 THAI DIGIT SIX
    "Thai_lekchet":                  0x0df7,  # U+0E57 THAI DIGIT SEVEN
    "Thai_lekpaet":                  0x0df8,  # U+0E58 THAI DIGIT EIGHT
    "Thai_lekkao":                   0x0df9,  # U+0E59 THAI DIGIT NINE
    "Hangul":                        0xff31,  # Hangul start/stop(toggle)
    "Hangul_Start":                  0xff32,  # Hangul start
    "Hangul_End":                    0xff33,  # Hangul end, English start
    "Hangul_Hanja":                  0xff34,  # Start Hangul->Hanja Conversion
    "Hangul_Jamo":                   0xff35,  # Hangul Jamo mode
    "Hangul_Romaja":                 0xff36,  # Hangul Romaja mode
    "Hangul_Codeinput":              0xff37,  # Hangul code input mode
    "Hangul_Jeonja":                 0xff38,  # Jeonja mode
    "Hangul_Banja":                  0xff39,  # Banja mode
    "Hangul_PreHanja":               0xff3a,  # Pre Hanja conversion
    "Hangul_PostHanja":              0xff3b,  # Post Hanja conversion
    "Hangul_SingleCandidate":        0xff3c,  # Single candidate
    "Hangul_MultipleCandidate":      0xff3d,  # Multiple candidate
    "Hangul_PreviousCandidate":      0xff3e,  # Previous candidate
    "Hangul_Special":                0xff3f,  # Special symbols
    "Hangul_switch":                 0xff7e,  # Alias for mode_switch
    "Hangul_Kiyeog":                 0x0ea1,  # U+3131 HANGUL LETTER KIYEOK
    "Hangul_SsangKiyeog":            0x0ea2,  # U+3132 HANGUL LETTER SSANGKIYEOK
    "Hangul_KiyeogSios":             0x0ea3,  # U+3133 HANGUL LETTER KIYEOK-SIOS
    "Hangul_Nieun":                  0x0ea4,  # U+3134 HANGUL LETTER NIEUN
    "Hangul_NieunJieuj":             0x0ea5,  # U+3135 HANGUL LETTER NIEUN-CIEUC
    "Hangul_NieunHieuh":             0x0ea6,  # U+3136 HANGUL LETTER NIEUN-HIEUH
    "Hangul_Dikeud":                 0x0ea7,  # U+3137 HANGUL LETTER TIKEUT
    "Hangul_SsangDikeud":            0x0ea8,  # U+3138 HANGUL LETTER SSANGTIKEUT
    "Hangul_Rieul":                  0x0ea9,  # U+3139 HANGUL LETTER RIEUL
    "Hangul_RieulKiyeog":            0x0eaa,  # U+313A HANGUL LETTER RIEUL-KIYEOK
    "Hangul_RieulMieum":             0x0eab,  # U+313B HANGUL LETTER RIEUL-MIEUM
    "Hangul_RieulPieub":             0x0eac,  # U+313C HANGUL LETTER RIEUL-PIEUP
    "Hangul_RieulSios":              0x0ead,  # U+313D HANGUL LETTER RIEUL-SIOS
    "Hangul_RieulTieut":             0x0eae,  # U+313E HANGUL LETTER RIEUL-THIEUTH
    "Hangul_RieulPhieuf":            0x0eaf,  # U+313F HANGUL LETTER RIEUL-PHIEUPH
    "Hangul_RieulHieuh":             0x0eb0,  # U+3140 HANGUL LETTER RIEUL-HIEUH
    "Hangul_Mieum":                  0x0eb1,  # U+3141 HANGUL LETTER MIEUM
    "Hangul_Pieub":                  0x0eb2,  # U+3142 HANGUL LETTER PIEUP
    "Hangul_SsangPieub":             0x0eb3,  # U+3143 HANGUL LETTER SSANGPIEUP
    "Hangul_PieubSios":              0x0eb4,  # U+3144 HANGUL LETTER PIEUP-SIOS
    "Hangul_Sios":                   0x0eb5,  # U+3145 HANGUL LETTER SIOS
    "Hangul_SsangSios":              0x0eb6,  # U+3146 HANGUL LETTER SSANGSIOS
    "Hangul_Ieung":                  0x0eb7,  # U+3147 HANGUL LETTER IEUNG
    "Hangul_Jieuj":                  0x0eb8,  # U+3148 HANGUL LETTER CIEUC
    "Hangul_SsangJieuj":             0x0eb9,  # U+3149 HANGUL LETTER SSANGCIEUC
    "Hangul_Cieuc":                  0x0eba,  # U+314A HANGUL LETTER CHIEUCH
    "Hangul_Khieuq":                 0x0ebb,  # U+314B HANGUL LETTER KHIEUKH
    "Hangul_Tieut":                  0x0ebc,  # U+314C HANGUL LETTER THIEUTH
    "Hangul_Phieuf":                 0x0ebd,  # U+314D HANGUL LETTER PHIEUPH
    "Hangul_Hieuh":                  0x0ebe,  # U+314E HANGUL LETTER HIEUH
    "Hangul_A":                      0x0ebf,  # U+314F HANGUL LETTER A
    "Hangul_AE":                     0x0ec0,  # U+3150 HANGUL LETTER AE
    "Hangul_YA":                     0x0ec1,  # U+3151 HANGUL LETTER YA
    "Hangul_YAE":                    0x0ec2,  # U+3152 HANGUL LETTER YAE
    "Hangul_EO":                     0x0ec3,  # U+3153 HANGUL LETTER EO
    "Hangul_E":                      0x0ec4,  # U+3154 HANGUL LETTER E
    "Hangul_YEO":                    0x0ec5,  # U+3155 HANGUL LETTER YEO
    "Hangul_YE":                     0x0ec6,  # U+3156 HANGUL LETTER YE
    "Hangul_O":                      0x0ec7,  # U+3157 HANGUL LETTER O
    "Hangul_WA":                     0x0ec8,  # U+3158 HANGUL LETTER WA
    "Hangul_WAE":                    0x0ec9,  # U+3159 HANGUL LETTER WAE
    "Hangul_OE":                     0x0eca,  # U+315A HANGUL LETTER OE
    "Hangul_YO":                     0x0ecb,  # U+315B HANGUL LETTER YO
    "Hangul_U":                      0x0ecc,  # U+315C HANGUL LETTER U
    "Hangul_WEO":                    0x0ecd,  # U+315D HANGUL LETTER WEO
    "Hangul_WE":                     0x0ece,  # U+315E HANGUL LETTER WE
    "Hangul_WI":                     0x0ecf,  # U+315F HANGUL LETTER WI
    "Hangul_YU":                     0x0ed0,  # U+3160 HANGUL LETTER YU
    "Hangul_EU":                     0x0ed1,  # U+3161 HANGUL LETTER EU
    "Hangul_YI":                     0x0ed2,  # U+3162 HANGUL LETTER YI
    "Hangul_I":                      0x0ed3,  # U+3163 HANGUL LETTER I
    "Hangul_J_Kiyeog":               0x0ed4,  # U+11A8 HANGUL JONGSEONG KIYEOK
    "Hangul_J_SsangKiyeog":          0x0ed5,  # U+11A9 HANGUL JONGSEONG SSANGKIYEOK
    "Hangul_J_KiyeogSios":           0x0ed6,  # U+11AA HANGUL JONGSEONG KIYEOK-SIOS
    "Hangul_J_Nieun":                0x0ed7,  # U+11AB HANGUL JONGSEONG NIEUN
    "Hangul_J_NieunJieuj":           0x0ed8,  # U+11AC HANGUL JONGSEONG NIEUN-CIEUC
    "Hangul_J_NieunHieuh":           0x0ed9,  # U+11AD HANGUL JONGSEONG NIEUN-HIEUH
    "Hangul_J_Dikeud":               0x0eda,  # U+11AE HANGUL JONGSEONG TIKEUT
    "Hangul_J_Rieul":                0x0edb,  # U+11AF HANGUL JONGSEONG RIEUL
    "Hangul_J_RieulKiyeog":          0x0edc,  # U+11B0 HANGUL JONGSEONG RIEUL-KIYEOK
    "Hangul_J_RieulMieum":           0x0edd,  # U+11B1 HANGUL JONGSEONG RIEUL-MIEUM
    "Hangul_J_RieulPieub":           0x0ede,  # U+11B2 HANGUL JONGSEONG RIEUL-PIEUP
    "Hangul_J_RieulSios":            0x0edf,  # U+11B3 HANGUL JONGSEONG RIEUL-SIOS
    "Hangul_J_RieulTieut":           0x0ee0,  # U+11B4 HANGUL JONGSEONG RIEUL-THIEUTH
    "Hangul_J_RieulPhieuf":          0x0ee1,  # U+11B5 HANGUL JONGSEONG RIEUL-PHIEUPH
    "Hangul_J_RieulHieuh":           0x0ee2,  # U+11B6 HANGUL JONGSEONG RIEUL-HIEUH
    "Hangul_J_Mieum":                0x0ee3,  # U+11B7 HANGUL JONGSEONG MIEUM
    "Hangul_J_Pieub":                0x0ee4,  # U+11B8 HANGUL JONGSEONG PIEUP
    "Hangul_J_PieubSios":            0x0ee5,  # U+11B9 HANGUL JONGSEONG PIEUP-SIOS
    "Hangul_J_Sios":                 0x0ee6,  # U+11BA HANGUL JONGSEONG SIOS
    "Hangul_J_SsangSios":            0x0ee7,  # U+11BB HANGUL JONGSEONG SSANGSIOS
    "Hangul_J_Ieung":                0x0ee8,  # U+11BC HANGUL JONGSEONG IEUNG
    "Hangul_J_Jieuj":                0x0ee9,  # U+11BD HANGUL JONGSEONG CIEUC
    "Hangul_J_Cieuc":                0x0eea,  # U+11BE HANGUL JONGSEONG CHIEUCH
    "Hangul_J_Khieuq":               0x0eeb,  # U+11BF HANGUL JONGSEONG KHIEUKH
    "Hangul_J_Tieut":                0x0eec,  # U+11C0 HANGUL JONGSEONG THIEUTH
    "Hangul_J_Phieuf":               0x0eed,  # U+11C1 HANGUL JONGSEONG PHIEUPH
    "Hangul_J_Hieuh":                0x0eee,  # U+11C2 HANGUL JONGSEONG HIEUH
    "Hangul_RieulYeorinHieuh":       0x0eef,  # U+316D HANGUL LETTER RIEUL-YEORINHIEUH
    "Hangul_SunkyeongeumMieum":      0x0ef0,  # U+3171 HANGUL LETTER KAPYEOUNMIEUM
    "Hangul_SunkyeongeumPieub":      0x0ef1,  # U+3178 HANGUL LETTER KAPYEOUNPIEUP
    "Hangul_PanSios":                0x0ef2,  # U+317F HANGUL LETTER PANSIOS
    "Hangul_KkogjiDalrinIeung":      0x0ef3,  # U+3181 HANGUL LETTER YESIEUNG
    "Hangul_SunkyeongeumPhieuf":     0x0ef4,  # U+3184 HANGUL LETTER KAPYEOUNPHIEUPH
    "Hangul_YeorinHieuh":            0x0ef5,  # U+3186 HANGUL LETTER YEORINHIEUH
    "Hangul_AraeA":                  0x0ef6,  # U+318D HANGUL LETTER ARAEA
    "Hangul_AraeAE":                 0x0ef7,  # U+318E HANGUL LETTER ARAEAE
    "Hangul_J_PanSios":              0x0ef8,  # U+11EB HANGUL JONGSEONG PANSIOS
    "Hangul_J_KkogjiDalrinIeung":    0x0ef9,  # U+11F0 HANGUL JONGSEONG YESIEUNG
    "Hangul_J_YeorinHieuh":          0x0efa,  # U+11F9 HANGUL JONGSEONG YEORINHIEUH
    "Korean_Won":                    0x0eff,  #(U+20A9 WON SIGN)
    "Armenian_ligature_ew":       0x1000587,  # U+0587 ARMENIAN SMALL LIGATURE ECH YIWN
    "Armenian_full_stop":         0x1000589,  # U+0589 ARMENIAN FULL STOP
    "Armenian_verjaket":          0x1000589,  # U+0589 ARMENIAN FULL STOP
    "Armenian_separation_mark":   0x100055d,  # U+055D ARMENIAN COMMA
    "Armenian_but":               0x100055d,  # U+055D ARMENIAN COMMA
    "Armenian_hyphen":            0x100058a,  # U+058A ARMENIAN HYPHEN
    "Armenian_yentamna":          0x100058a,  # U+058A ARMENIAN HYPHEN
    "Armenian_exclam":            0x100055c,  # U+055C ARMENIAN EXCLAMATION MARK
    "Armenian_amanak":            0x100055c,  # U+055C ARMENIAN EXCLAMATION MARK
    "Armenian_accent":            0x100055b,  # U+055B ARMENIAN EMPHASIS MARK
    "Armenian_shesht":            0x100055b,  # U+055B ARMENIAN EMPHASIS MARK
    "Armenian_question":          0x100055e,  # U+055E ARMENIAN QUESTION MARK
    "Armenian_paruyk":            0x100055e,  # U+055E ARMENIAN QUESTION MARK
    "Armenian_AYB":               0x1000531,  # U+0531 ARMENIAN CAPITAL LETTER AYB
    "Armenian_ayb":               0x1000561,  # U+0561 ARMENIAN SMALL LETTER AYB
    "Armenian_BEN":               0x1000532,  # U+0532 ARMENIAN CAPITAL LETTER BEN
    "Armenian_ben":               0x1000562,  # U+0562 ARMENIAN SMALL LETTER BEN
    "Armenian_GIM":               0x1000533,  # U+0533 ARMENIAN CAPITAL LETTER GIM
    "Armenian_gim":               0x1000563,  # U+0563 ARMENIAN SMALL LETTER GIM
    "Armenian_DA":                0x1000534,  # U+0534 ARMENIAN CAPITAL LETTER DA
    "Armenian_da":                0x1000564,  # U+0564 ARMENIAN SMALL LETTER DA
    "Armenian_YECH":              0x1000535,  # U+0535 ARMENIAN CAPITAL LETTER ECH
    "Armenian_yech":              0x1000565,  # U+0565 ARMENIAN SMALL LETTER ECH
    "Armenian_ZA":                0x1000536,  # U+0536 ARMENIAN CAPITAL LETTER ZA
    "Armenian_za":                0x1000566,  # U+0566 ARMENIAN SMALL LETTER ZA
    "Armenian_E":                 0x1000537,  # U+0537 ARMENIAN CAPITAL LETTER EH
    "Armenian_e":                 0x1000567,  # U+0567 ARMENIAN SMALL LETTER EH
    "Armenian_AT":                0x1000538,  # U+0538 ARMENIAN CAPITAL LETTER ET
    "Armenian_at":                0x1000568,  # U+0568 ARMENIAN SMALL LETTER ET
    "Armenian_TO":                0x1000539,  # U+0539 ARMENIAN CAPITAL LETTER TO
    "Armenian_to":                0x1000569,  # U+0569 ARMENIAN SMALL LETTER TO
    "Armenian_ZHE":               0x100053a,  # U+053A ARMENIAN CAPITAL LETTER ZHE
    "Armenian_zhe":               0x100056a,  # U+056A ARMENIAN SMALL LETTER ZHE
    "Armenian_INI":               0x100053b,  # U+053B ARMENIAN CAPITAL LETTER INI
    "Armenian_ini":               0x100056b,  # U+056B ARMENIAN SMALL LETTER INI
    "Armenian_LYUN":              0x100053c,  # U+053C ARMENIAN CAPITAL LETTER LIWN
    "Armenian_lyun":              0x100056c,  # U+056C ARMENIAN SMALL LETTER LIWN
    "Armenian_KHE":               0x100053d,  # U+053D ARMENIAN CAPITAL LETTER XEH
    "Armenian_khe":               0x100056d,  # U+056D ARMENIAN SMALL LETTER XEH
    "Armenian_TSA":               0x100053e,  # U+053E ARMENIAN CAPITAL LETTER CA
    "Armenian_tsa":               0x100056e,  # U+056E ARMENIAN SMALL LETTER CA
    "Armenian_KEN":               0x100053f,  # U+053F ARMENIAN CAPITAL LETTER KEN
    "Armenian_ken":               0x100056f,  # U+056F ARMENIAN SMALL LETTER KEN
    "Armenian_HO":                0x1000540,  # U+0540 ARMENIAN CAPITAL LETTER HO
    "Armenian_ho":                0x1000570,  # U+0570 ARMENIAN SMALL LETTER HO
    "Armenian_DZA":               0x1000541,  # U+0541 ARMENIAN CAPITAL LETTER JA
    "Armenian_dza":               0x1000571,  # U+0571 ARMENIAN SMALL LETTER JA
    "Armenian_GHAT":              0x1000542,  # U+0542 ARMENIAN CAPITAL LETTER GHAD
    "Armenian_ghat":              0x1000572,  # U+0572 ARMENIAN SMALL LETTER GHAD
    "Armenian_TCHE":              0x1000543,  # U+0543 ARMENIAN CAPITAL LETTER CHEH
    "Armenian_tche":              0x1000573,  # U+0573 ARMENIAN SMALL LETTER CHEH
    "Armenian_MEN":               0x1000544,  # U+0544 ARMENIAN CAPITAL LETTER MEN
    "Armenian_men":               0x1000574,  # U+0574 ARMENIAN SMALL LETTER MEN
    "Armenian_HI":                0x1000545,  # U+0545 ARMENIAN CAPITAL LETTER YI
    "Armenian_hi":                0x1000575,  # U+0575 ARMENIAN SMALL LETTER YI
    "Armenian_NU":                0x1000546,  # U+0546 ARMENIAN CAPITAL LETTER NOW
    "Armenian_nu":                0x1000576,  # U+0576 ARMENIAN SMALL LETTER NOW
    "Armenian_SHA":               0x1000547,  # U+0547 ARMENIAN CAPITAL LETTER SHA
    "Armenian_sha":               0x1000577,  # U+0577 ARMENIAN SMALL LETTER SHA
    "Armenian_VO":                0x1000548,  # U+0548 ARMENIAN CAPITAL LETTER VO
    "Armenian_vo":                0x1000578,  # U+0578 ARMENIAN SMALL LETTER VO
    "Armenian_CHA":               0x1000549,  # U+0549 ARMENIAN CAPITAL LETTER CHA
    "Armenian_cha":               0x1000579,  # U+0579 ARMENIAN SMALL LETTER CHA
    "Armenian_PE":                0x100054a,  # U+054A ARMENIAN CAPITAL LETTER PEH
    "Armenian_pe":                0x100057a,  # U+057A ARMENIAN SMALL LETTER PEH
    "Armenian_JE":                0x100054b,  # U+054B ARMENIAN CAPITAL LETTER JHEH
    "Armenian_je":                0x100057b,  # U+057B ARMENIAN SMALL LETTER JHEH
    "Armenian_RA":                0x100054c,  # U+054C ARMENIAN CAPITAL LETTER RA
    "Armenian_ra":                0x100057c,  # U+057C ARMENIAN SMALL LETTER RA
    "Armenian_SE":                0x100054d,  # U+054D ARMENIAN CAPITAL LETTER SEH
    "Armenian_se":                0x100057d,  # U+057D ARMENIAN SMALL LETTER SEH
    "Armenian_VEV":               0x100054e,  # U+054E ARMENIAN CAPITAL LETTER VEW
    "Armenian_vev":               0x100057e,  # U+057E ARMENIAN SMALL LETTER VEW
    "Armenian_TYUN":              0x100054f,  # U+054F ARMENIAN CAPITAL LETTER TIWN
    "Armenian_tyun":              0x100057f,  # U+057F ARMENIAN SMALL LETTER TIWN
    "Armenian_RE":                0x1000550,  # U+0550 ARMENIAN CAPITAL LETTER REH
    "Armenian_re":                0x1000580,  # U+0580 ARMENIAN SMALL LETTER REH
    "Armenian_TSO":               0x1000551,  # U+0551 ARMENIAN CAPITAL LETTER CO
    "Armenian_tso":               0x1000581,  # U+0581 ARMENIAN SMALL LETTER CO
    "Armenian_VYUN":              0x1000552,  # U+0552 ARMENIAN CAPITAL LETTER YIWN
    "Armenian_vyun":              0x1000582,  # U+0582 ARMENIAN SMALL LETTER YIWN
    "Armenian_PYUR":              0x1000553,  # U+0553 ARMENIAN CAPITAL LETTER PIWR
    "Armenian_pyur":              0x1000583,  # U+0583 ARMENIAN SMALL LETTER PIWR
    "Armenian_KE":                0x1000554,  # U+0554 ARMENIAN CAPITAL LETTER KEH
    "Armenian_ke":                0x1000584,  # U+0584 ARMENIAN SMALL LETTER KEH
    "Armenian_O":                 0x1000555,  # U+0555 ARMENIAN CAPITAL LETTER OH
    "Armenian_o":                 0x1000585,  # U+0585 ARMENIAN SMALL LETTER OH
    "Armenian_FE":                0x1000556,  # U+0556 ARMENIAN CAPITAL LETTER FEH
    "Armenian_fe":                0x1000586,  # U+0586 ARMENIAN SMALL LETTER FEH
    "Armenian_apostrophe":        0x100055a,  # U+055A ARMENIAN APOSTROPHE
    "Georgian_an":                0x10010d0,  # U+10D0 GEORGIAN LETTER AN
    "Georgian_ban":               0x10010d1,  # U+10D1 GEORGIAN LETTER BAN
    "Georgian_gan":               0x10010d2,  # U+10D2 GEORGIAN LETTER GAN
    "Georgian_don":               0x10010d3,  # U+10D3 GEORGIAN LETTER DON
    "Georgian_en":                0x10010d4,  # U+10D4 GEORGIAN LETTER EN
    "Georgian_vin":               0x10010d5,  # U+10D5 GEORGIAN LETTER VIN
    "Georgian_zen":               0x10010d6,  # U+10D6 GEORGIAN LETTER ZEN
    "Georgian_tan":               0x10010d7,  # U+10D7 GEORGIAN LETTER TAN
    "Georgian_in":                0x10010d8,  # U+10D8 GEORGIAN LETTER IN
    "Georgian_kan":               0x10010d9,  # U+10D9 GEORGIAN LETTER KAN
    "Georgian_las":               0x10010da,  # U+10DA GEORGIAN LETTER LAS
    "Georgian_man":               0x10010db,  # U+10DB GEORGIAN LETTER MAN
    "Georgian_nar":               0x10010dc,  # U+10DC GEORGIAN LETTER NAR
    "Georgian_on":                0x10010dd,  # U+10DD GEORGIAN LETTER ON
    "Georgian_par":               0x10010de,  # U+10DE GEORGIAN LETTER PAR
    "Georgian_zhar":              0x10010df,  # U+10DF GEORGIAN LETTER ZHAR
    "Georgian_rae":               0x10010e0,  # U+10E0 GEORGIAN LETTER RAE
    "Georgian_san":               0x10010e1,  # U+10E1 GEORGIAN LETTER SAN
    "Georgian_tar":               0x10010e2,  # U+10E2 GEORGIAN LETTER TAR
    "Georgian_un":                0x10010e3,  # U+10E3 GEORGIAN LETTER UN
    "Georgian_phar":              0x10010e4,  # U+10E4 GEORGIAN LETTER PHAR
    "Georgian_khar":              0x10010e5,  # U+10E5 GEORGIAN LETTER KHAR
    "Georgian_ghan":              0x10010e6,  # U+10E6 GEORGIAN LETTER GHAN
    "Georgian_qar":               0x10010e7,  # U+10E7 GEORGIAN LETTER QAR
    "Georgian_shin":              0x10010e8,  # U+10E8 GEORGIAN LETTER SHIN
    "Georgian_chin":              0x10010e9,  # U+10E9 GEORGIAN LETTER CHIN
    "Georgian_can":               0x10010ea,  # U+10EA GEORGIAN LETTER CAN
    "Georgian_jil":               0x10010eb,  # U+10EB GEORGIAN LETTER JIL
    "Georgian_cil":               0x10010ec,  # U+10EC GEORGIAN LETTER CIL
    "Georgian_char":              0x10010ed,  # U+10ED GEORGIAN LETTER CHAR
    "Georgian_xan":               0x10010ee,  # U+10EE GEORGIAN LETTER XAN
    "Georgian_jhan":              0x10010ef,  # U+10EF GEORGIAN LETTER JHAN
    "Georgian_hae":               0x10010f0,  # U+10F0 GEORGIAN LETTER HAE
    "Georgian_he":                0x10010f1,  # U+10F1 GEORGIAN LETTER HE
    "Georgian_hie":               0x10010f2,  # U+10F2 GEORGIAN LETTER HIE
    "Georgian_we":                0x10010f3,  # U+10F3 GEORGIAN LETTER WE
    "Georgian_har":               0x10010f4,  # U+10F4 GEORGIAN LETTER HAR
    "Georgian_hoe":               0x10010f5,  # U+10F5 GEORGIAN LETTER HOE
    "Georgian_fi":                0x10010f6,  # U+10F6 GEORGIAN LETTER FI
    "Xabovedot":                  0x1001e8a,  # U+1E8A LATIN CAPITAL LETTER X WITH DOT ABOVE
    "Ibreve":                     0x100012c,  # U+012C LATIN CAPITAL LETTER I WITH BREVE
    "Zstroke":                    0x10001b5,  # U+01B5 LATIN CAPITAL LETTER Z WITH STROKE
    "Gcaron":                     0x10001e6,  # U+01E6 LATIN CAPITAL LETTER G WITH CARON
    "Ocaron":                     0x10001d1,  # U+01D1 LATIN CAPITAL LETTER O WITH CARON
    "Obarred":                    0x100019f,  # U+019F LATIN CAPITAL LETTER O WITH MIDDLE TILDE
    "xabovedot":                  0x1001e8b,  # U+1E8B LATIN SMALL LETTER X WITH DOT ABOVE
    "ibreve":                     0x100012d,  # U+012D LATIN SMALL LETTER I WITH BREVE
    "zstroke":                    0x10001b6,  # U+01B6 LATIN SMALL LETTER Z WITH STROKE
    "gcaron":                     0x10001e7,  # U+01E7 LATIN SMALL LETTER G WITH CARON
    "ocaron":                     0x10001d2,  # U+01D2 LATIN SMALL LETTER O WITH CARON
    "obarred":                    0x1000275,  # U+0275 LATIN SMALL LETTER BARRED O
    "SCHWA":                      0x100018f,  # U+018F LATIN CAPITAL LETTER SCHWA
    "schwa":                      0x1000259,  # U+0259 LATIN SMALL LETTER SCHWA
    "EZH":                        0x10001b7,  # U+01B7 LATIN CAPITAL LETTER EZH
    "ezh":                        0x1000292,  # U+0292 LATIN SMALL LETTER EZH
    "Lbelowdot":                  0x1001e36,  # U+1E36 LATIN CAPITAL LETTER L WITH DOT BELOW
    "lbelowdot":                  0x1001e37,  # U+1E37 LATIN SMALL LETTER L WITH DOT BELOW
    "Abelowdot":                  0x1001ea0,  # U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW
    "abelowdot":                  0x1001ea1,  # U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW
    "Ahook":                      0x1001ea2,  # U+1EA2 LATIN CAPITAL LETTER A WITH HOOK ABOVE
    "ahook":                      0x1001ea3,  # U+1EA3 LATIN SMALL LETTER A WITH HOOK ABOVE
    "Acircumflexacute":           0x1001ea4,  # U+1EA4 LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND ACUTE
    "acircumflexacute":           0x1001ea5,  # U+1EA5 LATIN SMALL LETTER A WITH CIRCUMFLEX AND ACUTE
    "Acircumflexgrave":           0x1001ea6,  # U+1EA6 LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND GRAVE
    "acircumflexgrave":           0x1001ea7,  # U+1EA7 LATIN SMALL LETTER A WITH CIRCUMFLEX AND GRAVE
    "Acircumflexhook":            0x1001ea8,  # U+1EA8 LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
    "acircumflexhook":            0x1001ea9,  # U+1EA9 LATIN SMALL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
    "Acircumflextilde":           0x1001eaa,  # U+1EAA LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND TILDE
    "acircumflextilde":           0x1001eab,  # U+1EAB LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE
    "Acircumflexbelowdot":        0x1001eac,  # U+1EAC LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND DOT BELOW
    "acircumflexbelowdot":        0x1001ead,  # U+1EAD LATIN SMALL LETTER A WITH CIRCUMFLEX AND DOT BELOW
    "Abreveacute":                0x1001eae,  # U+1EAE LATIN CAPITAL LETTER A WITH BREVE AND ACUTE
    "abreveacute":                0x1001eaf,  # U+1EAF LATIN SMALL LETTER A WITH BREVE AND ACUTE
    "Abrevegrave":                0x1001eb0,  # U+1EB0 LATIN CAPITAL LETTER A WITH BREVE AND GRAVE
    "abrevegrave":                0x1001eb1,  # U+1EB1 LATIN SMALL LETTER A WITH BREVE AND GRAVE
    "Abrevehook":                 0x1001eb2,  # U+1EB2 LATIN CAPITAL LETTER A WITH BREVE AND HOOK ABOVE
    "abrevehook":                 0x1001eb3,  # U+1EB3 LATIN SMALL LETTER A WITH BREVE AND HOOK ABOVE
    "Abrevetilde":                0x1001eb4,  # U+1EB4 LATIN CAPITAL LETTER A WITH BREVE AND TILDE
    "abrevetilde":                0x1001eb5,  # U+1EB5 LATIN SMALL LETTER A WITH BREVE AND TILDE
    "Abrevebelowdot":             0x1001eb6,  # U+1EB6 LATIN CAPITAL LETTER A WITH BREVE AND DOT BELOW
    "abrevebelowdot":             0x1001eb7,  # U+1EB7 LATIN SMALL LETTER A WITH BREVE AND DOT BELOW
    "Ebelowdot":                  0x1001eb8,  # U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW
    "ebelowdot":                  0x1001eb9,  # U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW
    "Ehook":                      0x1001eba,  # U+1EBA LATIN CAPITAL LETTER E WITH HOOK ABOVE
    "ehook":                      0x1001ebb,  # U+1EBB LATIN SMALL LETTER E WITH HOOK ABOVE
    "Etilde":                     0x1001ebc,  # U+1EBC LATIN CAPITAL LETTER E WITH TILDE
    "etilde":                     0x1001ebd,  # U+1EBD LATIN SMALL LETTER E WITH TILDE
    "Ecircumflexacute":           0x1001ebe,  # U+1EBE LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND ACUTE
    "ecircumflexacute":           0x1001ebf,  # U+1EBF LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE
    "Ecircumflexgrave":           0x1001ec0,  # U+1EC0 LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND GRAVE
    "ecircumflexgrave":           0x1001ec1,  # U+1EC1 LATIN SMALL LETTER E WITH CIRCUMFLEX AND GRAVE
    "Ecircumflexhook":            0x1001ec2,  # U+1EC2 LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
    "ecircumflexhook":            0x1001ec3,  # U+1EC3 LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
    "Ecircumflextilde":           0x1001ec4,  # U+1EC4 LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND TILDE
    "ecircumflextilde":           0x1001ec5,  # U+1EC5 LATIN SMALL LETTER E WITH CIRCUMFLEX AND TILDE
    "Ecircumflexbelowdot":        0x1001ec6,  # U+1EC6 LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND DOT BELOW
    "ecircumflexbelowdot":        0x1001ec7,  # U+1EC7 LATIN SMALL LETTER E WITH CIRCUMFLEX AND DOT BELOW
    "Ihook":                      0x1001ec8,  # U+1EC8 LATIN CAPITAL LETTER I WITH HOOK ABOVE
    "ihook":                      0x1001ec9,  # U+1EC9 LATIN SMALL LETTER I WITH HOOK ABOVE
    "Ibelowdot":                  0x1001eca,  # U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW
    "ibelowdot":                  0x1001ecb,  # U+1ECB LATIN SMALL LETTER I WITH DOT BELOW
    "Obelowdot":                  0x1001ecc,  # U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW
    "obelowdot":                  0x1001ecd,  # U+1ECD LATIN SMALL LETTER O WITH DOT BELOW
    "Ohook":                      0x1001ece,  # U+1ECE LATIN CAPITAL LETTER O WITH HOOK ABOVE
    "ohook":                      0x1001ecf,  # U+1ECF LATIN SMALL LETTER O WITH HOOK ABOVE
    "Ocircumflexacute":           0x1001ed0,  # U+1ED0 LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND ACUTE
    "ocircumflexacute":           0x1001ed1,  # U+1ED1 LATIN SMALL LETTER O WITH CIRCUMFLEX AND ACUTE
    "Ocircumflexgrave":           0x1001ed2,  # U+1ED2 LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND GRAVE
    "ocircumflexgrave":           0x1001ed3,  # U+1ED3 LATIN SMALL LETTER O WITH CIRCUMFLEX AND GRAVE
    "Ocircumflexhook":            0x1001ed4,  # U+1ED4 LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
    "ocircumflexhook":            0x1001ed5,  # U+1ED5 LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
    "Ocircumflextilde":           0x1001ed6,  # U+1ED6 LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND TILDE
    "ocircumflextilde":           0x1001ed7,  # U+1ED7 LATIN SMALL LETTER O WITH CIRCUMFLEX AND TILDE
    "Ocircumflexbelowdot":        0x1001ed8,  # U+1ED8 LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND DOT BELOW
    "ocircumflexbelowdot":        0x1001ed9,  # U+1ED9 LATIN SMALL LETTER O WITH CIRCUMFLEX AND DOT BELOW
    "Ohornacute":                 0x1001eda,  # U+1EDA LATIN CAPITAL LETTER O WITH HORN AND ACUTE
    "ohornacute":                 0x1001edb,  # U+1EDB LATIN SMALL LETTER O WITH HORN AND ACUTE
    "Ohorngrave":                 0x1001edc,  # U+1EDC LATIN CAPITAL LETTER O WITH HORN AND GRAVE
    "ohorngrave":                 0x1001edd,  # U+1EDD LATIN SMALL LETTER O WITH HORN AND GRAVE
    "Ohornhook":                  0x1001ede,  # U+1EDE LATIN CAPITAL LETTER O WITH HORN AND HOOK ABOVE
    "ohornhook":                  0x1001edf,  # U+1EDF LATIN SMALL LETTER O WITH HORN AND HOOK ABOVE
    "Ohorntilde":                 0x1001ee0,  # U+1EE0 LATIN CAPITAL LETTER O WITH HORN AND TILDE
    "ohorntilde":                 0x1001ee1,  # U+1EE1 LATIN SMALL LETTER O WITH HORN AND TILDE
    "Ohornbelowdot":              0x1001ee2,  # U+1EE2 LATIN CAPITAL LETTER O WITH HORN AND DOT BELOW
    "ohornbelowdot":              0x1001ee3,  # U+1EE3 LATIN SMALL LETTER O WITH HORN AND DOT BELOW
    "Ubelowdot":                  0x1001ee4,  # U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW
    "ubelowdot":                  0x1001ee5,  # U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW
    "Uhook":                      0x1001ee6,  # U+1EE6 LATIN CAPITAL LETTER U WITH HOOK ABOVE
    "uhook":                      0x1001ee7,  # U+1EE7 LATIN SMALL LETTER U WITH HOOK ABOVE
    "Uhornacute":                 0x1001ee8,  # U+1EE8 LATIN CAPITAL LETTER U WITH HORN AND ACUTE
    "uhornacute":                 0x1001ee9,  # U+1EE9 LATIN SMALL LETTER U WITH HORN AND ACUTE
    "Uhorngrave":                 0x1001eea,  # U+1EEA LATIN CAPITAL LETTER U WITH HORN AND GRAVE
    "uhorngrave":                 0x1001eeb,  # U+1EEB LATIN SMALL LETTER U WITH HORN AND GRAVE
    "Uhornhook":                  0x1001eec,  # U+1EEC LATIN CAPITAL LETTER U WITH HORN AND HOOK ABOVE
    "uhornhook":                  0x1001eed,  # U+1EED LATIN SMALL LETTER U WITH HORN AND HOOK ABOVE
    "Uhorntilde":                 0x1001eee,  # U+1EEE LATIN CAPITAL LETTER U WITH HORN AND TILDE
    "uhorntilde":                 0x1001eef,  # U+1EEF LATIN SMALL LETTER U WITH HORN AND TILDE
    "Uhornbelowdot":              0x1001ef0,  # U+1EF0 LATIN CAPITAL LETTER U WITH HORN AND DOT BELOW
    "uhornbelowdot":              0x1001ef1,  # U+1EF1 LATIN SMALL LETTER U WITH HORN AND DOT BELOW
    "Ybelowdot":                  0x1001ef4,  # U+1EF4 LATIN CAPITAL LETTER Y WITH DOT BELOW
    "ybelowdot":                  0x1001ef5,  # U+1EF5 LATIN SMALL LETTER Y WITH DOT BELOW
    "Yhook":                      0x1001ef6,  # U+1EF6 LATIN CAPITAL LETTER Y WITH HOOK ABOVE
    "yhook":                      0x1001ef7,  # U+1EF7 LATIN SMALL LETTER Y WITH HOOK ABOVE
    "Ytilde":                     0x1001ef8,  # U+1EF8 LATIN CAPITAL LETTER Y WITH TILDE
    "ytilde":                     0x1001ef9,  # U+1EF9 LATIN SMALL LETTER Y WITH TILDE
    "Ohorn":                      0x10001a0,  # U+01A0 LATIN CAPITAL LETTER O WITH HORN
    "ohorn":                      0x10001a1,  # U+01A1 LATIN SMALL LETTER O WITH HORN
    "Uhorn":                      0x10001af,  # U+01AF LATIN CAPITAL LETTER U WITH HORN
    "uhorn":                      0x10001b0,  # U+01B0 LATIN SMALL LETTER U WITH HORN
    "combining_tilde":            0x1000303,  # U+0303 COMBINING TILDE
    "combining_grave":            0x1000300,  # U+0300 COMBINING GRAVE ACCENT
    "combining_acute":            0x1000301,  # U+0301 COMBINING ACUTE ACCENT
    "combining_hook":             0x1000309,  # U+0309 COMBINING HOOK ABOVE
    "combining_belowdot":         0x1000323,  # U+0323 COMBINING DOT BELOW
    "EcuSign":                    0x10020a0,  # U+20A0 EURO-CURRENCY SIGN
    "ColonSign":                  0x10020a1,  # U+20A1 COLON SIGN
    "CruzeiroSign":               0x10020a2,  # U+20A2 CRUZEIRO SIGN
    "FFrancSign":                 0x10020a3,  # U+20A3 FRENCH FRANC SIGN
    "LiraSign":                   0x10020a4,  # U+20A4 LIRA SIGN
    "MillSign":                   0x10020a5,  # U+20A5 MILL SIGN
    "NairaSign":                  0x10020a6,  # U+20A6 NAIRA SIGN
    "PesetaSign":                 0x10020a7,  # U+20A7 PESETA SIGN
    "RupeeSign":                  0x10020a8,  # U+20A8 RUPEE SIGN
    "WonSign":                    0x10020a9,  # U+20A9 WON SIGN
    "NewSheqelSign":              0x10020aa,  # U+20AA NEW SHEQEL SIGN
    "DongSign":                   0x10020ab,  # U+20AB DONG SIGN
    "EuroSign":                      0x20ac,  # U+20AC EURO SIGN
    "zerosuperior":               0x1002070,  # U+2070 SUPERSCRIPT ZERO
    "foursuperior":               0x1002074,  # U+2074 SUPERSCRIPT FOUR
    "fivesuperior":               0x1002075,  # U+2075 SUPERSCRIPT FIVE
    "sixsuperior":                0x1002076,  # U+2076 SUPERSCRIPT SIX
    "sevensuperior":              0x1002077,  # U+2077 SUPERSCRIPT SEVEN
    "eightsuperior":              0x1002078,  # U+2078 SUPERSCRIPT EIGHT
    "ninesuperior":               0x1002079,  # U+2079 SUPERSCRIPT NINE
    "zerosubscript":              0x1002080,  # U+2080 SUBSCRIPT ZERO
    "onesubscript":               0x1002081,  # U+2081 SUBSCRIPT ONE
    "twosubscript":               0x1002082,  # U+2082 SUBSCRIPT TWO
    "threesubscript":             0x1002083,  # U+2083 SUBSCRIPT THREE
    "foursubscript":              0x1002084,  # U+2084 SUBSCRIPT FOUR
    "fivesubscript":              0x1002085,  # U+2085 SUBSCRIPT FIVE
    "sixsubscript":               0x1002086,  # U+2086 SUBSCRIPT SIX
    "sevensubscript":             0x1002087,  # U+2087 SUBSCRIPT SEVEN
    "eightsubscript":             0x1002088,  # U+2088 SUBSCRIPT EIGHT
    "ninesubscript":              0x1002089,  # U+2089 SUBSCRIPT NINE
    "partdifferential":           0x1002202,  # U+2202 PARTIAL DIFFERENTIAL
    "emptyset":                   0x1002205,  # U+2205 NULL SET
    "elementof":                  0x1002208,  # U+2208 ELEMENT OF
    "notelementof":               0x1002209,  # U+2209 NOT AN ELEMENT OF
    "containsas":                 0x100220B,  # U+220B CONTAINS AS MEMBER
    "squareroot":                 0x100221A,  # U+221A SQUARE ROOT
    "cuberoot":                   0x100221B,  # U+221B CUBE ROOT
    "fourthroot":                 0x100221C,  # U+221C FOURTH ROOT
    "dintegral":                  0x100222C,  # U+222C DOUBLE INTEGRAL
    "tintegral":                  0x100222D,  # U+222D TRIPLE INTEGRAL
    "because":                    0x1002235,  # U+2235 BECAUSE
    "approxeq":                   0x1002248,  #(U+2248 ALMOST EQUAL TO)
    "notapproxeq":                0x1002247,  #(U+2247 NEITHER APPROXIMATELY NOR ACTUALLY EQUAL TO)
    "notidentical":               0x1002262,  # U+2262 NOT IDENTICAL TO
    "stricteq":                   0x1002263,  # U+2263 STRICTLY EQUIVALENT TO
    "braille_dot_1":                 0xfff1,
    "braille_dot_2":                 0xfff2,
    "braille_dot_3":                 0xfff3,
    "braille_dot_4":                 0xfff4,
    "braille_dot_5":                 0xfff5,
    "braille_dot_6":                 0xfff6,
    "braille_dot_7":                 0xfff7,
    "braille_dot_8":                 0xfff8,
    "braille_dot_9":                 0xfff9,
    "braille_dot_10":                0xfffa,
    "braille_blank":              0x1002800,  # U+2800 BRAILLE PATTERN BLANK
    "braille_dots_1":             0x1002801,  # U+2801 BRAILLE PATTERN DOTS-1
    "braille_dots_2":             0x1002802,  # U+2802 BRAILLE PATTERN DOTS-2
    "braille_dots_12":            0x1002803,  # U+2803 BRAILLE PATTERN DOTS-12
    "braille_dots_3":             0x1002804,  # U+2804 BRAILLE PATTERN DOTS-3
    "braille_dots_13":            0x1002805,  # U+2805 BRAILLE PATTERN DOTS-13
    "braille_dots_23":            0x1002806,  # U+2806 BRAILLE PATTERN DOTS-23
    "braille_dots_123":           0x1002807,  # U+2807 BRAILLE PATTERN DOTS-123
    "braille_dots_4":             0x1002808,  # U+2808 BRAILLE PATTERN DOTS-4
    "braille_dots_14":            0x1002809,  # U+2809 BRAILLE PATTERN DOTS-14
    "braille_dots_24":            0x100280a,  # U+280a BRAILLE PATTERN DOTS-24
    "braille_dots_124":           0x100280b,  # U+280b BRAILLE PATTERN DOTS-124
    "braille_dots_34":            0x100280c,  # U+280c BRAILLE PATTERN DOTS-34
    "braille_dots_134":           0x100280d,  # U+280d BRAILLE PATTERN DOTS-134
    "braille_dots_234":           0x100280e,  # U+280e BRAILLE PATTERN DOTS-234
    "braille_dots_1234":          0x100280f,  # U+280f BRAILLE PATTERN DOTS-1234
    "braille_dots_5":             0x1002810,  # U+2810 BRAILLE PATTERN DOTS-5
    "braille_dots_15":            0x1002811,  # U+2811 BRAILLE PATTERN DOTS-15
    "braille_dots_25":            0x1002812,  # U+2812 BRAILLE PATTERN DOTS-25
    "braille_dots_125":           0x1002813,  # U+2813 BRAILLE PATTERN DOTS-125
    "braille_dots_35":            0x1002814,  # U+2814 BRAILLE PATTERN DOTS-35
    "braille_dots_135":           0x1002815,  # U+2815 BRAILLE PATTERN DOTS-135
    "braille_dots_235":           0x1002816,  # U+2816 BRAILLE PATTERN DOTS-235
    "braille_dots_1235":          0x1002817,  # U+2817 BRAILLE PATTERN DOTS-1235
    "braille_dots_45":            0x1002818,  # U+2818 BRAILLE PATTERN DOTS-45
    "braille_dots_145":           0x1002819,  # U+2819 BRAILLE PATTERN DOTS-145
    "braille_dots_245":           0x100281a,  # U+281a BRAILLE PATTERN DOTS-245
    "braille_dots_1245":          0x100281b,  # U+281b BRAILLE PATTERN DOTS-1245
    "braille_dots_345":           0x100281c,  # U+281c BRAILLE PATTERN DOTS-345
    "braille_dots_1345":          0x100281d,  # U+281d BRAILLE PATTERN DOTS-1345
    "braille_dots_2345":          0x100281e,  # U+281e BRAILLE PATTERN DOTS-2345
    "braille_dots_12345":         0x100281f,  # U+281f BRAILLE PATTERN DOTS-12345
    "braille_dots_6":             0x1002820,  # U+2820 BRAILLE PATTERN DOTS-6
    "braille_dots_16":            0x1002821,  # U+2821 BRAILLE PATTERN DOTS-16
    "braille_dots_26":            0x1002822,  # U+2822 BRAILLE PATTERN DOTS-26
    "braille_dots_126":           0x1002823,  # U+2823 BRAILLE PATTERN DOTS-126
    "braille_dots_36":            0x1002824,  # U+2824 BRAILLE PATTERN DOTS-36
    "braille_dots_136":           0x1002825,  # U+2825 BRAILLE PATTERN DOTS-136
    "braille_dots_236":           0x1002826,  # U+2826 BRAILLE PATTERN DOTS-236
    "braille_dots_1236":          0x1002827,  # U+2827 BRAILLE PATTERN DOTS-1236
    "braille_dots_46":            0x1002828,  # U+2828 BRAILLE PATTERN DOTS-46
    "braille_dots_146":           0x1002829,  # U+2829 BRAILLE PATTERN DOTS-146
    "braille_dots_246":           0x100282a,  # U+282a BRAILLE PATTERN DOTS-246
    "braille_dots_1246":          0x100282b,  # U+282b BRAILLE PATTERN DOTS-1246
    "braille_dots_346":           0x100282c,  # U+282c BRAILLE PATTERN DOTS-346
    "braille_dots_1346":          0x100282d,  # U+282d BRAILLE PATTERN DOTS-1346
    "braille_dots_2346":          0x100282e,  # U+282e BRAILLE PATTERN DOTS-2346
    "braille_dots_12346":         0x100282f,  # U+282f BRAILLE PATTERN DOTS-12346
    "braille_dots_56":            0x1002830,  # U+2830 BRAILLE PATTERN DOTS-56
    "braille_dots_156":           0x1002831,  # U+2831 BRAILLE PATTERN DOTS-156
    "braille_dots_256":           0x1002832,  # U+2832 BRAILLE PATTERN DOTS-256
    "braille_dots_1256":          0x1002833,  # U+2833 BRAILLE PATTERN DOTS-1256
    "braille_dots_356":           0x1002834,  # U+2834 BRAILLE PATTERN DOTS-356
    "braille_dots_1356":          0x1002835,  # U+2835 BRAILLE PATTERN DOTS-1356
    "braille_dots_2356":          0x1002836,  # U+2836 BRAILLE PATTERN DOTS-2356
    "braille_dots_12356":         0x1002837,  # U+2837 BRAILLE PATTERN DOTS-12356
    "braille_dots_456":           0x1002838,  # U+2838 BRAILLE PATTERN DOTS-456
    "braille_dots_1456":          0x1002839,  # U+2839 BRAILLE PATTERN DOTS-1456
    "braille_dots_2456":          0x100283a,  # U+283a BRAILLE PATTERN DOTS-2456
    "braille_dots_12456":         0x100283b,  # U+283b BRAILLE PATTERN DOTS-12456
    "braille_dots_3456":          0x100283c,  # U+283c BRAILLE PATTERN DOTS-3456
    "braille_dots_13456":         0x100283d,  # U+283d BRAILLE PATTERN DOTS-13456
    "braille_dots_23456":         0x100283e,  # U+283e BRAILLE PATTERN DOTS-23456
    "braille_dots_123456":        0x100283f,  # U+283f BRAILLE PATTERN DOTS-123456
    "braille_dots_7":             0x1002840,  # U+2840 BRAILLE PATTERN DOTS-7
    "braille_dots_17":            0x1002841,  # U+2841 BRAILLE PATTERN DOTS-17
    "braille_dots_27":            0x1002842,  # U+2842 BRAILLE PATTERN DOTS-27
    "braille_dots_127":           0x1002843,  # U+2843 BRAILLE PATTERN DOTS-127
    "braille_dots_37":            0x1002844,  # U+2844 BRAILLE PATTERN DOTS-37
    "braille_dots_137":           0x1002845,  # U+2845 BRAILLE PATTERN DOTS-137
    "braille_dots_237":           0x1002846,  # U+2846 BRAILLE PATTERN DOTS-237
    "braille_dots_1237":          0x1002847,  # U+2847 BRAILLE PATTERN DOTS-1237
    "braille_dots_47":            0x1002848,  # U+2848 BRAILLE PATTERN DOTS-47
    "braille_dots_147":           0x1002849,  # U+2849 BRAILLE PATTERN DOTS-147
    "braille_dots_247":           0x100284a,  # U+284a BRAILLE PATTERN DOTS-247
    "braille_dots_1247":          0x100284b,  # U+284b BRAILLE PATTERN DOTS-1247
    "braille_dots_347":           0x100284c,  # U+284c BRAILLE PATTERN DOTS-347
    "braille_dots_1347":          0x100284d,  # U+284d BRAILLE PATTERN DOTS-1347
    "braille_dots_2347":          0x100284e,  # U+284e BRAILLE PATTERN DOTS-2347
    "braille_dots_12347":         0x100284f,  # U+284f BRAILLE PATTERN DOTS-12347
    "braille_dots_57":            0x1002850,  # U+2850 BRAILLE PATTERN DOTS-57
    "braille_dots_157":           0x1002851,  # U+2851 BRAILLE PATTERN DOTS-157
    "braille_dots_257":           0x1002852,  # U+2852 BRAILLE PATTERN DOTS-257
    "braille_dots_1257":          0x1002853,  # U+2853 BRAILLE PATTERN DOTS-1257
    "braille_dots_357":           0x1002854,  # U+2854 BRAILLE PATTERN DOTS-357
    "braille_dots_1357":          0x1002855,  # U+2855 BRAILLE PATTERN DOTS-1357
    "braille_dots_2357":          0x1002856,  # U+2856 BRAILLE PATTERN DOTS-2357
    "braille_dots_12357":         0x1002857,  # U+2857 BRAILLE PATTERN DOTS-12357
    "braille_dots_457":           0x1002858,  # U+2858 BRAILLE PATTERN DOTS-457
    "braille_dots_1457":          0x1002859,  # U+2859 BRAILLE PATTERN DOTS-1457
    "braille_dots_2457":          0x100285a,  # U+285a BRAILLE PATTERN DOTS-2457
    "braille_dots_12457":         0x100285b,  # U+285b BRAILLE PATTERN DOTS-12457
    "braille_dots_3457":          0x100285c,  # U+285c BRAILLE PATTERN DOTS-3457
    "braille_dots_13457":         0x100285d,  # U+285d BRAILLE PATTERN DOTS-13457
    "braille_dots_23457":         0x100285e,  # U+285e BRAILLE PATTERN DOTS-23457
    "braille_dots_123457":        0x100285f,  # U+285f BRAILLE PATTERN DOTS-123457
    "braille_dots_67":            0x1002860,  # U+2860 BRAILLE PATTERN DOTS-67
    "braille_dots_167":           0x1002861,  # U+2861 BRAILLE PATTERN DOTS-167
    "braille_dots_267":           0x1002862,  # U+2862 BRAILLE PATTERN DOTS-267
    "braille_dots_1267":          0x1002863,  # U+2863 BRAILLE PATTERN DOTS-1267
    "braille_dots_367":           0x1002864,  # U+2864 BRAILLE PATTERN DOTS-367
    "braille_dots_1367":          0x1002865,  # U+2865 BRAILLE PATTERN DOTS-1367
    "braille_dots_2367":          0x1002866,  # U+2866 BRAILLE PATTERN DOTS-2367
    "braille_dots_12367":         0x1002867,  # U+2867 BRAILLE PATTERN DOTS-12367
    "braille_dots_467":           0x1002868,  # U+2868 BRAILLE PATTERN DOTS-467
    "braille_dots_1467":          0x1002869,  # U+2869 BRAILLE PATTERN DOTS-1467
    "braille_dots_2467":          0x100286a,  # U+286a BRAILLE PATTERN DOTS-2467
    "braille_dots_12467":         0x100286b,  # U+286b BRAILLE PATTERN DOTS-12467
    "braille_dots_3467":          0x100286c,  # U+286c BRAILLE PATTERN DOTS-3467
    "braille_dots_13467":         0x100286d,  # U+286d BRAILLE PATTERN DOTS-13467
    "braille_dots_23467":         0x100286e,  # U+286e BRAILLE PATTERN DOTS-23467
    "braille_dots_123467":        0x100286f,  # U+286f BRAILLE PATTERN DOTS-123467
    "braille_dots_567":           0x1002870,  # U+2870 BRAILLE PATTERN DOTS-567
    "braille_dots_1567":          0x1002871,  # U+2871 BRAILLE PATTERN DOTS-1567
    "braille_dots_2567":          0x1002872,  # U+2872 BRAILLE PATTERN DOTS-2567
    "braille_dots_12567":         0x1002873,  # U+2873 BRAILLE PATTERN DOTS-12567
    "braille_dots_3567":          0x1002874,  # U+2874 BRAILLE PATTERN DOTS-3567
    "braille_dots_13567":         0x1002875,  # U+2875 BRAILLE PATTERN DOTS-13567
    "braille_dots_23567":         0x1002876,  # U+2876 BRAILLE PATTERN DOTS-23567
    "braille_dots_123567":        0x1002877,  # U+2877 BRAILLE PATTERN DOTS-123567
    "braille_dots_4567":          0x1002878,  # U+2878 BRAILLE PATTERN DOTS-4567
    "braille_dots_14567":         0x1002879,  # U+2879 BRAILLE PATTERN DOTS-14567
    "braille_dots_24567":         0x100287a,  # U+287a BRAILLE PATTERN DOTS-24567
    "braille_dots_124567":        0x100287b,  # U+287b BRAILLE PATTERN DOTS-124567
    "braille_dots_34567":         0x100287c,  # U+287c BRAILLE PATTERN DOTS-34567
    "braille_dots_134567":        0x100287d,  # U+287d BRAILLE PATTERN DOTS-134567
    "braille_dots_234567":        0x100287e,  # U+287e BRAILLE PATTERN DOTS-234567
    "braille_dots_1234567":       0x100287f,  # U+287f BRAILLE PATTERN DOTS-1234567
    "braille_dots_8":             0x1002880,  # U+2880 BRAILLE PATTERN DOTS-8
    "braille_dots_18":            0x1002881,  # U+2881 BRAILLE PATTERN DOTS-18
    "braille_dots_28":            0x1002882,  # U+2882 BRAILLE PATTERN DOTS-28
    "braille_dots_128":           0x1002883,  # U+2883 BRAILLE PATTERN DOTS-128
    "braille_dots_38":            0x1002884,  # U+2884 BRAILLE PATTERN DOTS-38
    "braille_dots_138":           0x1002885,  # U+2885 BRAILLE PATTERN DOTS-138
    "braille_dots_238":           0x1002886,  # U+2886 BRAILLE PATTERN DOTS-238
    "braille_dots_1238":          0x1002887,  # U+2887 BRAILLE PATTERN DOTS-1238
    "braille_dots_48":            0x1002888,  # U+2888 BRAILLE PATTERN DOTS-48
    "braille_dots_148":           0x1002889,  # U+2889 BRAILLE PATTERN DOTS-148
    "braille_dots_248":           0x100288a,  # U+288a BRAILLE PATTERN DOTS-248
    "braille_dots_1248":          0x100288b,  # U+288b BRAILLE PATTERN DOTS-1248
    "braille_dots_348":           0x100288c,  # U+288c BRAILLE PATTERN DOTS-348
    "braille_dots_1348":          0x100288d,  # U+288d BRAILLE PATTERN DOTS-1348
    "braille_dots_2348":          0x100288e,  # U+288e BRAILLE PATTERN DOTS-2348
    "braille_dots_12348":         0x100288f,  # U+288f BRAILLE PATTERN DOTS-12348
    "braille_dots_58":            0x1002890,  # U+2890 BRAILLE PATTERN DOTS-58
    "braille_dots_158":           0x1002891,  # U+2891 BRAILLE PATTERN DOTS-158
    "braille_dots_258":           0x1002892,  # U+2892 BRAILLE PATTERN DOTS-258
    "braille_dots_1258":          0x1002893,  # U+2893 BRAILLE PATTERN DOTS-1258
    "braille_dots_358":           0x1002894,  # U+2894 BRAILLE PATTERN DOTS-358
    "braille_dots_1358":          0x1002895,  # U+2895 BRAILLE PATTERN DOTS-1358
    "braille_dots_2358":          0x1002896,  # U+2896 BRAILLE PATTERN DOTS-2358
    "braille_dots_12358":         0x1002897,  # U+2897 BRAILLE PATTERN DOTS-12358
    "braille_dots_458":           0x1002898,  # U+2898 BRAILLE PATTERN DOTS-458
    "braille_dots_1458":          0x1002899,  # U+2899 BRAILLE PATTERN DOTS-1458
    "braille_dots_2458":          0x100289a,  # U+289a BRAILLE PATTERN DOTS-2458
    "braille_dots_12458":         0x100289b,  # U+289b BRAILLE PATTERN DOTS-12458
    "braille_dots_3458":          0x100289c,  # U+289c BRAILLE PATTERN DOTS-3458
    "braille_dots_13458":         0x100289d,  # U+289d BRAILLE PATTERN DOTS-13458
    "braille_dots_23458":         0x100289e,  # U+289e BRAILLE PATTERN DOTS-23458
    "braille_dots_123458":        0x100289f,  # U+289f BRAILLE PATTERN DOTS-123458
    "braille_dots_68":            0x10028a0,  # U+28a0 BRAILLE PATTERN DOTS-68
    "braille_dots_168":           0x10028a1,  # U+28a1 BRAILLE PATTERN DOTS-168
    "braille_dots_268":           0x10028a2,  # U+28a2 BRAILLE PATTERN DOTS-268
    "braille_dots_1268":          0x10028a3,  # U+28a3 BRAILLE PATTERN DOTS-1268
    "braille_dots_368":           0x10028a4,  # U+28a4 BRAILLE PATTERN DOTS-368
    "braille_dots_1368":          0x10028a5,  # U+28a5 BRAILLE PATTERN DOTS-1368
    "braille_dots_2368":          0x10028a6,  # U+28a6 BRAILLE PATTERN DOTS-2368
    "braille_dots_12368":         0x10028a7,  # U+28a7 BRAILLE PATTERN DOTS-12368
    "braille_dots_468":           0x10028a8,  # U+28a8 BRAILLE PATTERN DOTS-468
    "braille_dots_1468":          0x10028a9,  # U+28a9 BRAILLE PATTERN DOTS-1468
    "braille_dots_2468":          0x10028aa,  # U+28aa BRAILLE PATTERN DOTS-2468
    "braille_dots_12468":         0x10028ab,  # U+28ab BRAILLE PATTERN DOTS-12468
    "braille_dots_3468":          0x10028ac,  # U+28ac BRAILLE PATTERN DOTS-3468
    "braille_dots_13468":         0x10028ad,  # U+28ad BRAILLE PATTERN DOTS-13468
    "braille_dots_23468":         0x10028ae,  # U+28ae BRAILLE PATTERN DOTS-23468
    "braille_dots_123468":        0x10028af,  # U+28af BRAILLE PATTERN DOTS-123468
    "braille_dots_568":           0x10028b0,  # U+28b0 BRAILLE PATTERN DOTS-568
    "braille_dots_1568":          0x10028b1,  # U+28b1 BRAILLE PATTERN DOTS-1568
    "braille_dots_2568":          0x10028b2,  # U+28b2 BRAILLE PATTERN DOTS-2568
    "braille_dots_12568":         0x10028b3,  # U+28b3 BRAILLE PATTERN DOTS-12568
    "braille_dots_3568":          0x10028b4,  # U+28b4 BRAILLE PATTERN DOTS-3568
    "braille_dots_13568":         0x10028b5,  # U+28b5 BRAILLE PATTERN DOTS-13568
    "braille_dots_23568":         0x10028b6,  # U+28b6 BRAILLE PATTERN DOTS-23568
    "braille_dots_123568":        0x10028b7,  # U+28b7 BRAILLE PATTERN DOTS-123568
    "braille_dots_4568":          0x10028b8,  # U+28b8 BRAILLE PATTERN DOTS-4568
    "braille_dots_14568":         0x10028b9,  # U+28b9 BRAILLE PATTERN DOTS-14568
    "braille_dots_24568":         0x10028ba,  # U+28ba BRAILLE PATTERN DOTS-24568
    "braille_dots_124568":        0x10028bb,  # U+28bb BRAILLE PATTERN DOTS-124568
    "braille_dots_34568":         0x10028bc,  # U+28bc BRAILLE PATTERN DOTS-34568
    "braille_dots_134568":        0x10028bd,  # U+28bd BRAILLE PATTERN DOTS-134568
    "braille_dots_234568":        0x10028be,  # U+28be BRAILLE PATTERN DOTS-234568
    "braille_dots_1234568":       0x10028bf,  # U+28bf BRAILLE PATTERN DOTS-1234568
    "braille_dots_78":            0x10028c0,  # U+28c0 BRAILLE PATTERN DOTS-78
    "braille_dots_178":           0x10028c1,  # U+28c1 BRAILLE PATTERN DOTS-178
    "braille_dots_278":           0x10028c2,  # U+28c2 BRAILLE PATTERN DOTS-278
    "braille_dots_1278":          0x10028c3,  # U+28c3 BRAILLE PATTERN DOTS-1278
    "braille_dots_378":           0x10028c4,  # U+28c4 BRAILLE PATTERN DOTS-378
    "braille_dots_1378":          0x10028c5,  # U+28c5 BRAILLE PATTERN DOTS-1378
    "braille_dots_2378":          0x10028c6,  # U+28c6 BRAILLE PATTERN DOTS-2378
    "braille_dots_12378":         0x10028c7,  # U+28c7 BRAILLE PATTERN DOTS-12378
    "braille_dots_478":           0x10028c8,  # U+28c8 BRAILLE PATTERN DOTS-478
    "braille_dots_1478":          0x10028c9,  # U+28c9 BRAILLE PATTERN DOTS-1478
    "braille_dots_2478":          0x10028ca,  # U+28ca BRAILLE PATTERN DOTS-2478
    "braille_dots_12478":         0x10028cb,  # U+28cb BRAILLE PATTERN DOTS-12478
    "braille_dots_3478":          0x10028cc,  # U+28cc BRAILLE PATTERN DOTS-3478
    "braille_dots_13478":         0x10028cd,  # U+28cd BRAILLE PATTERN DOTS-13478
    "braille_dots_23478":         0x10028ce,  # U+28ce BRAILLE PATTERN DOTS-23478
    "braille_dots_123478":        0x10028cf,  # U+28cf BRAILLE PATTERN DOTS-123478
    "braille_dots_578":           0x10028d0,  # U+28d0 BRAILLE PATTERN DOTS-578
    "braille_dots_1578":          0x10028d1,  # U+28d1 BRAILLE PATTERN DOTS-1578
    "braille_dots_2578":          0x10028d2,  # U+28d2 BRAILLE PATTERN DOTS-2578
    "braille_dots_12578":         0x10028d3,  # U+28d3 BRAILLE PATTERN DOTS-12578
    "braille_dots_3578":          0x10028d4,  # U+28d4 BRAILLE PATTERN DOTS-3578
    "braille_dots_13578":         0x10028d5,  # U+28d5 BRAILLE PATTERN DOTS-13578
    "braille_dots_23578":         0x10028d6,  # U+28d6 BRAILLE PATTERN DOTS-23578
    "braille_dots_123578":        0x10028d7,  # U+28d7 BRAILLE PATTERN DOTS-123578
    "braille_dots_4578":          0x10028d8,  # U+28d8 BRAILLE PATTERN DOTS-4578
    "braille_dots_14578":         0x10028d9,  # U+28d9 BRAILLE PATTERN DOTS-14578
    "braille_dots_24578":         0x10028da,  # U+28da BRAILLE PATTERN DOTS-24578
    "braille_dots_124578":        0x10028db,  # U+28db BRAILLE PATTERN DOTS-124578
    "braille_dots_34578":         0x10028dc,  # U+28dc BRAILLE PATTERN DOTS-34578
    "braille_dots_134578":        0x10028dd,  # U+28dd BRAILLE PATTERN DOTS-134578
    "braille_dots_234578":        0x10028de,  # U+28de BRAILLE PATTERN DOTS-234578
    "braille_dots_1234578":       0x10028df,  # U+28df BRAILLE PATTERN DOTS-1234578
    "braille_dots_678":           0x10028e0,  # U+28e0 BRAILLE PATTERN DOTS-678
    "braille_dots_1678":          0x10028e1,  # U+28e1 BRAILLE PATTERN DOTS-1678
    "braille_dots_2678":          0x10028e2,  # U+28e2 BRAILLE PATTERN DOTS-2678
    "braille_dots_12678":         0x10028e3,  # U+28e3 BRAILLE PATTERN DOTS-12678
    "braille_dots_3678":          0x10028e4,  # U+28e4 BRAILLE PATTERN DOTS-3678
    "braille_dots_13678":         0x10028e5,  # U+28e5 BRAILLE PATTERN DOTS-13678
    "braille_dots_23678":         0x10028e6,  # U+28e6 BRAILLE PATTERN DOTS-23678
    "braille_dots_123678":        0x10028e7,  # U+28e7 BRAILLE PATTERN DOTS-123678
    "braille_dots_4678":          0x10028e8,  # U+28e8 BRAILLE PATTERN DOTS-4678
    "braille_dots_14678":         0x10028e9,  # U+28e9 BRAILLE PATTERN DOTS-14678
    "braille_dots_24678":         0x10028ea,  # U+28ea BRAILLE PATTERN DOTS-24678
    "braille_dots_124678":        0x10028eb,  # U+28eb BRAILLE PATTERN DOTS-124678
    "braille_dots_34678":         0x10028ec,  # U+28ec BRAILLE PATTERN DOTS-34678
    "braille_dots_134678":        0x10028ed,  # U+28ed BRAILLE PATTERN DOTS-134678
    "braille_dots_234678":        0x10028ee,  # U+28ee BRAILLE PATTERN DOTS-234678
    "braille_dots_1234678":       0x10028ef,  # U+28ef BRAILLE PATTERN DOTS-1234678
    "braille_dots_5678":          0x10028f0,  # U+28f0 BRAILLE PATTERN DOTS-5678
    "braille_dots_15678":         0x10028f1,  # U+28f1 BRAILLE PATTERN DOTS-15678
    "braille_dots_25678":         0x10028f2,  # U+28f2 BRAILLE PATTERN DOTS-25678
    "braille_dots_125678":        0x10028f3,  # U+28f3 BRAILLE PATTERN DOTS-125678
    "braille_dots_35678":         0x10028f4,  # U+28f4 BRAILLE PATTERN DOTS-35678
    "braille_dots_135678":        0x10028f5,  # U+28f5 BRAILLE PATTERN DOTS-135678
    "braille_dots_235678":        0x10028f6,  # U+28f6 BRAILLE PATTERN DOTS-235678
    "braille_dots_1235678":       0x10028f7,  # U+28f7 BRAILLE PATTERN DOTS-1235678
    "braille_dots_45678":         0x10028f8,  # U+28f8 BRAILLE PATTERN DOTS-45678
    "braille_dots_145678":        0x10028f9,  # U+28f9 BRAILLE PATTERN DOTS-145678
    "braille_dots_245678":        0x10028fa,  # U+28fa BRAILLE PATTERN DOTS-245678
    "braille_dots_1245678":       0x10028fb,  # U+28fb BRAILLE PATTERN DOTS-1245678
    "braille_dots_345678":        0x10028fc,  # U+28fc BRAILLE PATTERN DOTS-345678
    "braille_dots_1345678":       0x10028fd,  # U+28fd BRAILLE PATTERN DOTS-1345678
    "braille_dots_2345678":       0x10028fe,  # U+28fe BRAILLE PATTERN DOTS-2345678
    "braille_dots_12345678":      0x10028ff,  # U+28ff BRAILLE PATTERN DOTS-12345678
    "Sinh_ng":            0x1000d82,  # U+0D82 SINHALA ANUSVARAYA
    "Sinh_h2":            0x1000d83,  # U+0D83 SINHALA VISARGAYA
    "Sinh_a":             0x1000d85,  # U+0D85 SINHALA AYANNA
    "Sinh_aa":            0x1000d86,  # U+0D86 SINHALA AAYANNA
    "Sinh_ae":            0x1000d87,  # U+0D87 SINHALA AEYANNA
    "Sinh_aee":           0x1000d88,  # U+0D88 SINHALA AEEYANNA
    "Sinh_i":             0x1000d89,  # U+0D89 SINHALA IYANNA
    "Sinh_ii":            0x1000d8a,  # U+0D8A SINHALA IIYANNA
    "Sinh_u":             0x1000d8b,  # U+0D8B SINHALA UYANNA
    "Sinh_uu":            0x1000d8c,  # U+0D8C SINHALA UUYANNA
    "Sinh_ri":            0x1000d8d,  # U+0D8D SINHALA IRUYANNA
    "Sinh_rii":           0x1000d8e,  # U+0D8E SINHALA IRUUYANNA
    "Sinh_lu":            0x1000d8f,  # U+0D8F SINHALA ILUYANNA
    "Sinh_luu":           0x1000d90,  # U+0D90 SINHALA ILUUYANNA
    "Sinh_e":             0x1000d91,  # U+0D91 SINHALA EYANNA
    "Sinh_ee":            0x1000d92,  # U+0D92 SINHALA EEYANNA
    "Sinh_ai":            0x1000d93,  # U+0D93 SINHALA AIYANNA
    "Sinh_o":             0x1000d94,  # U+0D94 SINHALA OYANNA
    "Sinh_oo":            0x1000d95,  # U+0D95 SINHALA OOYANNA
    "Sinh_au":            0x1000d96,  # U+0D96 SINHALA AUYANNA
    "Sinh_ka":            0x1000d9a,  # U+0D9A SINHALA KAYANNA
    "Sinh_kha":           0x1000d9b,  # U+0D9B SINHALA MAHA. KAYANNA
    "Sinh_ga":            0x1000d9c,  # U+0D9C SINHALA GAYANNA
    "Sinh_gha":           0x1000d9d,  # U+0D9D SINHALA MAHA. GAYANNA
    "Sinh_ng2":           0x1000d9e,  # U+0D9E SINHALA KANTAJA NAASIKYAYA
    "Sinh_nga":           0x1000d9f,  # U+0D9F SINHALA SANYAKA GAYANNA
    "Sinh_ca":            0x1000da0,  # U+0DA0 SINHALA CAYANNA
    "Sinh_cha":           0x1000da1,  # U+0DA1 SINHALA MAHA. CAYANNA
    "Sinh_ja":            0x1000da2,  # U+0DA2 SINHALA JAYANNA
    "Sinh_jha":           0x1000da3,  # U+0DA3 SINHALA MAHA. JAYANNA
    "Sinh_nya":           0x1000da4,  # U+0DA4 SINHALA TAALUJA NAASIKYAYA
    "Sinh_jnya":          0x1000da5,  # U+0DA5 SINHALA TAALUJA SANYOOGA NAASIKYAYA
    "Sinh_nja":           0x1000da6,  # U+0DA6 SINHALA SANYAKA JAYANNA
    "Sinh_tta":           0x1000da7,  # U+0DA7 SINHALA TTAYANNA
    "Sinh_ttha":          0x1000da8,  # U+0DA8 SINHALA MAHA. TTAYANNA
    "Sinh_dda":           0x1000da9,  # U+0DA9 SINHALA DDAYANNA
    "Sinh_ddha":          0x1000daa,  # U+0DAA SINHALA MAHA. DDAYANNA
    "Sinh_nna":           0x1000dab,  # U+0DAB SINHALA MUURDHAJA NAYANNA
    "Sinh_ndda":          0x1000dac,  # U+0DAC SINHALA SANYAKA DDAYANNA
    "Sinh_tha":           0x1000dad,  # U+0DAD SINHALA TAYANNA
    "Sinh_thha":          0x1000dae,  # U+0DAE SINHALA MAHA. TAYANNA
    "Sinh_dha":           0x1000daf,  # U+0DAF SINHALA DAYANNA
    "Sinh_dhha":          0x1000db0,  # U+0DB0 SINHALA MAHA. DAYANNA
    "Sinh_na":            0x1000db1,  # U+0DB1 SINHALA DANTAJA NAYANNA
    "Sinh_ndha":          0x1000db3,  # U+0DB3 SINHALA SANYAKA DAYANNA
    "Sinh_pa":            0x1000db4,  # U+0DB4 SINHALA PAYANNA
    "Sinh_pha":           0x1000db5,  # U+0DB5 SINHALA MAHA. PAYANNA
    "Sinh_ba":            0x1000db6,  # U+0DB6 SINHALA BAYANNA
    "Sinh_bha":           0x1000db7,  # U+0DB7 SINHALA MAHA. BAYANNA
    "Sinh_ma":            0x1000db8,  # U+0DB8 SINHALA MAYANNA
    "Sinh_mba":           0x1000db9,  # U+0DB9 SINHALA AMBA BAYANNA
    "Sinh_ya":            0x1000dba,  # U+0DBA SINHALA YAYANNA
    "Sinh_ra":            0x1000dbb,  # U+0DBB SINHALA RAYANNA
    "Sinh_la":            0x1000dbd,  # U+0DBD SINHALA DANTAJA LAYANNA
    "Sinh_va":            0x1000dc0,  # U+0DC0 SINHALA VAYANNA
    "Sinh_sha":           0x1000dc1,  # U+0DC1 SINHALA TAALUJA SAYANNA
    "Sinh_ssha":          0x1000dc2,  # U+0DC2 SINHALA MUURDHAJA SAYANNA
    "Sinh_sa":            0x1000dc3,  # U+0DC3 SINHALA DANTAJA SAYANNA
    "Sinh_ha":            0x1000dc4,  # U+0DC4 SINHALA HAYANNA
    "Sinh_lla":           0x1000dc5,  # U+0DC5 SINHALA MUURDHAJA LAYANNA
    "Sinh_fa":            0x1000dc6,  # U+0DC6 SINHALA FAYANNA
    "Sinh_al":            0x1000dca,  # U+0DCA SINHALA AL-LAKUNA
    "Sinh_aa2":           0x1000dcf,  # U+0DCF SINHALA AELA-PILLA
    "Sinh_ae2":           0x1000dd0,  # U+0DD0 SINHALA AEDA-PILLA
    "Sinh_aee2":          0x1000dd1,  # U+0DD1 SINHALA DIGA AEDA-PILLA
    "Sinh_i2":            0x1000dd2,  # U+0DD2 SINHALA IS-PILLA
    "Sinh_ii2":           0x1000dd3,  # U+0DD3 SINHALA DIGA IS-PILLA
    "Sinh_u2":            0x1000dd4,  # U+0DD4 SINHALA PAA-PILLA
    "Sinh_uu2":           0x1000dd6,  # U+0DD6 SINHALA DIGA PAA-PILLA
    "Sinh_ru2":           0x1000dd8,  # U+0DD8 SINHALA GAETTA-PILLA
    "Sinh_e2":            0x1000dd9,  # U+0DD9 SINHALA KOMBUVA
    "Sinh_ee2":           0x1000dda,  # U+0DDA SINHALA DIGA KOMBUVA
    "Sinh_ai2":           0x1000ddb,  # U+0DDB SINHALA KOMBU DEKA
    "Sinh_o2":            0x1000ddc,  # U+0DDC SINHALA KOMBUVA HAA AELA-PILLA
    "Sinh_oo2":           0x1000ddd,  # U+0DDD SINHALA KOMBUVA HAA DIGA AELA-PILLA
    "Sinh_au2":           0x1000dde,  # U+0DDE SINHALA KOMBUVA HAA GAYANUKITTA
    "Sinh_lu2":           0x1000ddf,  # U+0DDF SINHALA GAYANUKITTA
    "Sinh_ruu2":          0x1000df2,  # U+0DF2 SINHALA DIGA GAETTA-PILLA
    "Sinh_luu2":          0x1000df3,  # U+0DF3 SINHALA DIGA GAYANUKITTA
    "Sinh_kunddaliya":    0x1000df4,  # U+0DF4 SINHALA KUNDDALIYA
    "XF86ModeLock":		0x1008FF01,	# Mode Switch Lock
    "XF86MonBrightnessUp":    0x1008FF02,  # Monitor/panel brightness
    "XF86MonBrightnessDown":  0x1008FF03,  # Monitor/panel brightness
    "XF86KbdLightOnOff":      0x1008FF04,  # Keyboards may be lit
    "XF86KbdBrightnessUp":    0x1008FF05,  # Keyboards may be lit
    "XF86KbdBrightnessDown":  0x1008FF06,  # Keyboards may be lit
    "XF86MonBrightnessCycle": 0x1008FF07,  # Monitor/panel brightness
    "XF86Standby":		0x1008FF10,   # System into standby mode
    "XF86AudioLowerVolume":	0x1008FF11,   # Volume control down
    "XF86AudioMute":	0x1008FF12,   # Mute sound from the system
    "XF86AudioRaiseVolume":	0x1008FF13,   # Volume control up
    "XF86AudioPlay":	0x1008FF14,   # Start playing of audio >
    "XF86AudioStop":	0x1008FF15,   # Stop playing audio
    "XF86AudioPrev":	0x1008FF16,   # Previous track
    "XF86AudioNext":	0x1008FF17,   # Next track
    "XF86HomePage":		0x1008FF18,   # Display user's home page
    "XF86Mail":		0x1008FF19,   # Invoke user's mail program
    "XF86Start":		0x1008FF1A,   # Start application
    "XF86Search":		0x1008FF1B,   # Search
    "XF86AudioRecord":	0x1008FF1C,   # Record audio application
    "XF86Calculator":	0x1008FF1D,   # Invoke calculator program
    "XF86Memo":		0x1008FF1E,   # Invoke Memo taking program
    "XF86ToDoList":		0x1008FF1F,   # Invoke To Do List program
    "XF86Calendar":		0x1008FF20,   # Invoke Calendar program
    "XF86PowerDown":	0x1008FF21,   # Deep sleep the system
    "XF86ContrastAdjust":	0x1008FF22,   # Adjust screen contrast
    "XF86RockerUp":		0x1008FF23,   # Rocker switches exist up
    "XF86RockerDown":	0x1008FF24,   # and down
    "XF86RockerEnter":	0x1008FF25,   # and let you press them
    "XF86Back":		0x1008FF26,   # Like back on a browser
    "XF86Forward":		0x1008FF27,   # Like forward on a browser
    "XF86Stop":		0x1008FF28,   # Stop current operation
    "XF86Refresh":		0x1008FF29,   # Refresh the page
    "XF86PowerOff":		0x1008FF2A,   # Power off system entirely
    "XF86WakeUp":		0x1008FF2B,   # Wake up system from sleep
    "XF86Eject":            0x1008FF2C,   # Eject device (e.g. DVD)
    "XF86ScreenSaver":      0x1008FF2D,   # Invoke screensaver
    "XF86WWW":              0x1008FF2E,   # Invoke web browser
    "XF86Sleep":            0x1008FF2F,   # Put system to sleep
    "XF86Favorites":	0x1008FF30,   # Show favorite locations
    "XF86AudioPause":	0x1008FF31,   # Pause audio playing
    "XF86AudioMedia":	0x1008FF32,   # Launch media collection app
    "XF86MyComputer":	0x1008FF33,   # Display "My Computer" window
    "XF86VendorHome":	0x1008FF34,   # Display vendor home web site
    "XF86LightBulb":	0x1008FF35,   # Light bulb keys exist
    "XF86Shop":		0x1008FF36,   # Display shopping web site
    "XF86History":		0x1008FF37,   # Show history of web surfing
    "XF86OpenURL":		0x1008FF38,   # Open selected URL
    "XF86AddFavorite":	0x1008FF39,   # Add URL to favorites list
    "XF86HotLinks":		0x1008FF3A,   # Show "hot" links
    "XF86BrightnessAdjust":	0x1008FF3B,   # Invoke brightness adj. UI
    "XF86Finance":		0x1008FF3C,   # Display financial site
    "XF86Community":	0x1008FF3D,   # Display user's community
    "XF86AudioRewind":	0x1008FF3E,   # "rewind" audio track
    "XF86BackForward":	0x1008FF3F,   # ???
    "XF86Launch0":		0x1008FF40,   # Launch Application
    "XF86Launch1":		0x1008FF41,   # Launch Application
    "XF86Launch2":		0x1008FF42,   # Launch Application
    "XF86Launch3":		0x1008FF43,   # Launch Application
    "XF86Launch4":		0x1008FF44,   # Launch Application
    "XF86Launch5":		0x1008FF45,   # Launch Application
    "XF86Launch6":		0x1008FF46,   # Launch Application
    "XF86Launch7":		0x1008FF47,   # Launch Application
    "XF86Launch8":		0x1008FF48,   # Launch Application
    "XF86Launch9":		0x1008FF49,   # Launch Application
    "XF86LaunchA":		0x1008FF4A,   # Launch Application
    "XF86LaunchB":		0x1008FF4B,   # Launch Application
    "XF86LaunchC":		0x1008FF4C,   # Launch Application
    "XF86LaunchD":		0x1008FF4D,   # Launch Application
    "XF86LaunchE":		0x1008FF4E,   # Launch Application
    "XF86LaunchF":		0x1008FF4F,   # Launch Application
    "XF86ApplicationLeft":	0x1008FF50,   # switch to application, left
    "XF86ApplicationRight":	0x1008FF51,   # switch to application, right
    "XF86Book":		0x1008FF52,   # Launch bookreader
    "XF86CD":		0x1008FF53,   # Launch CD/DVD player
    "XF86Calculater":	0x1008FF54,   # Launch Calculater
    "XF86Clear":		0x1008FF55,   # Clear window, screen
    "XF86Close":		0x1008FF56,   # Close window
    "XF86Copy":		0x1008FF57,   # Copy selection
    "XF86Cut":		0x1008FF58,   # Cut selection
    "XF86Display":		0x1008FF59,   # Output switch key
    "XF86DOS":		0x1008FF5A,   # Launch DOS (emulation)
    "XF86Documents":	0x1008FF5B,   # Open documents window
    "XF86Excel":		0x1008FF5C,   # Launch spread sheet
    "XF86Explorer":		0x1008FF5D,   # Launch file explorer
    "XF86Game":		0x1008FF5E,   # Launch game
    "XF86Go":		0x1008FF5F,   # Go to URL
    "XF86iTouch":		0x1008FF60,   # Logitech iTouch- don't use
    "XF86LogOff":		0x1008FF61,   # Log off system
    "XF86Market":		0x1008FF62,   # ??
    "XF86Meeting":		0x1008FF63,   # enter meeting in calendar
    "XF86MenuKB":		0x1008FF65,   # distinguish keyboard from PB
    "XF86MenuPB":		0x1008FF66,   # distinguish PB from keyboard
    "XF86MySites":		0x1008FF67,   # Favourites
    "XF86New":		0x1008FF68,   # New (folder, document...
    "XF86News":		0x1008FF69,   # News
    "XF86OfficeHome":	0x1008FF6A,   # Office home (old Staroffice)
    "XF86Open":		0x1008FF6B,   # Open
    "XF86Option":		0x1008FF6C,   # ??
    "XF86Paste":		0x1008FF6D,   # Paste
    "XF86Phone":		0x1008FF6E,   # Launch phone; dial number
    "XF86Q":		0x1008FF70,   # Compaq's Q - don't use
    "XF86Reply":		0x1008FF72,   # Reply e.g., mail
    "XF86Reload":		0x1008FF73,   # Reload web page, file, etc.
    "XF86RotateWindows":	0x1008FF74,   # Rotate windows e.g. xrandr
    "XF86RotationPB":	0x1008FF75,   # don't use
    "XF86RotationKB":	0x1008FF76,   # don't use
    "XF86Save":		0x1008FF77,   # Save (file, document, state
    "XF86ScrollUp":		0x1008FF78,   # Scroll window/contents up
    "XF86ScrollDown":	0x1008FF79,   # Scrool window/contentd down
    "XF86ScrollClick":	0x1008FF7A,   # Use XKB mousekeys instead
    "XF86Send":		0x1008FF7B,   # Send mail, file, object
    "XF86Spell":		0x1008FF7C,   # Spell checker
    "XF86SplitScreen":	0x1008FF7D,   # Split window or screen
    "XF86Support":		0x1008FF7E,   # Get support (??)
    "XF86TaskPane":		0x1008FF7F,   # Show tasks
    "XF86Terminal":		0x1008FF80,   # Launch terminal emulator
    "XF86Tools":		0x1008FF81,   # toolbox of desktop/app.
    "XF86Travel":		0x1008FF82,   # ??
    "XF86UserPB":		0x1008FF84,   # ??
    "XF86User1KB":		0x1008FF85,   # ??
    "XF86User2KB":		0x1008FF86,   # ??
    "XF86Video":		0x1008FF87,   # Launch video player
    "XF86WheelButton":	0x1008FF88,   # button from a mouse wheel
    "XF86Word":		0x1008FF89,   # Launch word processor
    "XF86Xfer":		0x1008FF8A,
    "XF86ZoomIn":		0x1008FF8B,   # zoom in view, map, etc.
    "XF86ZoomOut":		0x1008FF8C,   # zoom out view, map, etc.
    "XF86Away":		0x1008FF8D,   # mark yourself as away
    "XF86Messenger":	0x1008FF8E,   # as in instant messaging
    "XF86WebCam":		0x1008FF8F,   # Launch web camera app.
    "XF86MailForward":	0x1008FF90,   # Forward in mail
    "XF86Pictures":		0x1008FF91,   # Show pictures
    "XF86Music":		0x1008FF92,   # Launch music application
    "XF86Battery":		0x1008FF93,   # Display battery information
    "XF86Bluetooth":	0x1008FF94,   # Enable/disable Bluetooth
    "XF86WLAN":		0x1008FF95,   # Enable/disable WLAN
    "XF86UWB":		0x1008FF96,   # Enable/disable UWB
    "XF86AudioForward":	0x1008FF97,   # fast-forward audio track
    "XF86AudioRepeat":	0x1008FF98,   # toggle repeat mode
    "XF86AudioRandomPlay":	0x1008FF99,   # toggle shuffle mode
    "XF86Subtitle":		0x1008FF9A,   # cycle through subtitle
    "XF86AudioCycleTrack":	0x1008FF9B,   # cycle through audio tracks
    "XF86CycleAngle":	0x1008FF9C,   # cycle through angles
    "XF86FrameBack":	0x1008FF9D,   # video: go one frame back
    "XF86FrameForward":	0x1008FF9E,   # video: go one frame forward
    "XF86Time":		0x1008FF9F,   # display, or shows an entry for time seeking
    "XF86Select":		0x1008FFA0,   # Select button on joypads and remotes
    "XF86View":		0x1008FFA1,   # Show a view options/properties
    "XF86TopMenu":		0x1008FFA2,   # Go to a top-level menu in a video
    "XF86Red":		0x1008FFA3,   # Red button
    "XF86Green":		0x1008FFA4,   # Green button
    "XF86Yellow":		0x1008FFA5,   # Yellow button
    "XF86Blue":             0x1008FFA6,   # Blue button
    "XF86Suspend":		0x1008FFA7,   # Sleep to RAM
    "XF86Hibernate":	0x1008FFA8,   # Sleep to disk
    "XF86TouchpadToggle":	0x1008FFA9,   # Toggle between touchpad/trackstick
    "XF86TouchpadOn":	0x1008FFB0,   # The touchpad got switched on
    "XF86TouchpadOff":	0x1008FFB1,   # The touchpad got switched off
    "XF86AudioMicMute":	0x1008FFB2,   # Mute the Mic from the system
    "XF86Keyboard":		0x1008FFB3,   # User defined keyboard related action
    "XF86WWAN":		0x1008FFB4,   # Toggle WWAN (LTE, UMTS, etc.) radio
    "XF86RFKill":		0x1008FFB5,   # Toggle radios on/off
    "XF86AudioPreset":	0x1008FFB6,   # Select equalizer preset, e.g. theatre-mode
    "XF86RotationLockToggle": 0x1008FFB7, # Toggle screen rotation lock on/off
    "XF86FullScreen":	0x1008FFB8,   # Toggle fullscreen
    "XF86Switch_VT_1":	0x1008FE01,
    "XF86Switch_VT_2":	0x1008FE02,
    "XF86Switch_VT_3":	0x1008FE03,
    "XF86Switch_VT_4":	0x1008FE04,
    "XF86Switch_VT_5":	0x1008FE05,
    "XF86Switch_VT_6":	0x1008FE06,
    "XF86Switch_VT_7":	0x1008FE07,
    "XF86Switch_VT_8":	0x1008FE08,
    "XF86Switch_VT_9":	0x1008FE09,
    "XF86Switch_VT_10":	0x1008FE0A,
    "XF86Switch_VT_11":	0x1008FE0B,
    "XF86Switch_VT_12":	0x1008FE0C,
    "XF86Ungrab":		0x1008FE20,   # force ungrab
    "XF86ClearGrab":	0x1008FE21,   # kill application with grab
    "XF86Next_VMode":	0x1008FE22,   # next video mode available
    "XF86Prev_VMode":	0x1008FE23,   # prev. video mode available
    "XF86LogWindowTree":	0x1008FE24,   # print window tree to log
    "XF86LogGrabInfo":	0x1008FE25,   # print all active grabs to log
    "XF86BrightnessAuto":		0x100810f4,		# v3.16 KEY_BRIGHTNESS_AUTO
    "XF86DisplayOff":		0x100810f5,		# v2.6.23 KEY_DISPLAY_OFF
    "XF86Info":			0x10081166,		#       KEY_INFO
    "XF86AspectRatio":		0x10081177,		# v5.1  KEY_ASPECT_RATIO
    "XF86DVD":			0x10081185,		#       KEY_DVD
    "XF86Audio":			0x10081188,		#       KEY_AUDIO
    "XF86ChannelUp":		0x10081192,		#       KEY_CHANNELUP
    "XF86ChannelDown":		0x10081193,		#       KEY_CHANNELDOWN
    "XF86Break":			0x1008119b,		#       KEY_BREAK
    "XF86VideoPhone":		0x100811a0,		# v2.6.20 KEY_VIDEOPHONE
    "XF86ZoomReset":		0x100811a4,		# v2.6.20 KEY_ZOOMRESET
    "XF86Editor":			0x100811a6,		# v2.6.20 KEY_EDITOR
    "XF86GraphicsEditor":		0x100811a8,		# v2.6.20 KEY_GRAPHICSEDITOR
    "XF86Presentation":		0x100811a9,		# v2.6.20 KEY_PRESENTATION
    "XF86Database":			0x100811aa,		# v2.6.20 KEY_DATABASE
    "XF86Voicemail":		0x100811ac,		# v2.6.20 KEY_VOICEMAIL
    "XF86Addressbook":		0x100811ad,		# v2.6.20 KEY_ADDRESSBOOK
    "XF86DisplayToggle":		0x100811af,		# v2.6.20 KEY_DISPLAYTOGGLE
    "XF86SpellCheck":		0x100811b0,		# v2.6.24 KEY_SPELLCHECK
    "XF86ContextMenu":		0x100811b6,		# v2.6.24 KEY_CONTEXT_MENU
    "XF86MediaRepeat":		0x100811b7,		# v2.6.26 KEY_MEDIA_REPEAT
    "XF8610ChannelsUp":		0x100811b8,		# v2.6.38 KEY_10CHANNELSUP
    "XF8610ChannelsDown":		0x100811b9,		# v2.6.38 KEY_10CHANNELSDOWN
    "XF86Images":			0x100811ba,		# v2.6.39 KEY_IMAGES
    "XF86NotificationCenter":	0x100811bc,		# v5.10 KEY_NOTIFICATION_CENTER
    "XF86PickupPhone":		0x100811bd,		# v5.10 KEY_PICKUP_PHONE
    "XF86HangupPhone":		0x100811be,		# v5.10 KEY_HANGUP_PHONE
    "XF86Fn":			0x100811d0,		#       KEY_FN
    "XF86Fn_Esc":			0x100811d1,		#       KEY_FN_ESC
    "XF86FnRightShift":		0x100811e5,		# v5.10 KEY_FN_RIGHT_SHIFT
    "XF86Numeric0":			0x10081200,		# v2.6.28 KEY_NUMERIC_0
    "XF86Numeric1":			0x10081201,		# v2.6.28 KEY_NUMERIC_1
    "XF86Numeric2":			0x10081202,		# v2.6.28 KEY_NUMERIC_2
    "XF86Numeric3":			0x10081203,		# v2.6.28 KEY_NUMERIC_3
    "XF86Numeric4":			0x10081204,		# v2.6.28 KEY_NUMERIC_4
    "XF86Numeric5":			0x10081205,		# v2.6.28 KEY_NUMERIC_5
    "XF86Numeric6":			0x10081206,		# v2.6.28 KEY_NUMERIC_6
    "XF86Numeric7":			0x10081207,		# v2.6.28 KEY_NUMERIC_7
    "XF86Numeric8":			0x10081208,		# v2.6.28 KEY_NUMERIC_8
    "XF86Numeric9":			0x10081209,		# v2.6.28 KEY_NUMERIC_9
    "XF86NumericStar":		0x1008120a,		# v2.6.28 KEY_NUMERIC_STAR
    "XF86NumericPound":		0x1008120b,		# v2.6.28 KEY_NUMERIC_POUND
    "XF86NumericA":			0x1008120c,		# v4.1  KEY_NUMERIC_A
    "XF86NumericB":			0x1008120d,		# v4.1  KEY_NUMERIC_B
    "XF86NumericC":			0x1008120e,		# v4.1  KEY_NUMERIC_C
    "XF86NumericD":			0x1008120f,		# v4.1  KEY_NUMERIC_D
    "XF86CameraFocus":		0x10081210,		# v2.6.33 KEY_CAMERA_FOCUS
    "XF86WPSButton":		0x10081211,		# v2.6.34 KEY_WPS_BUTTON
    "XF86CameraZoomIn":		0x10081215,		# v2.6.39 KEY_CAMERA_ZOOMIN
    "XF86CameraZoomOut":		0x10081216,		# v2.6.39 KEY_CAMERA_ZOOMOUT
    "XF86CameraUp":			0x10081217,		# v2.6.39 KEY_CAMERA_UP
    "XF86CameraDown":		0x10081218,		# v2.6.39 KEY_CAMERA_DOWN
    "XF86CameraLeft":		0x10081219,		# v2.6.39 KEY_CAMERA_LEFT
    "XF86CameraRight":		0x1008121a,		# v2.6.39 KEY_CAMERA_RIGHT
    "XF86AttendantOn":		0x1008121b,		# v3.10 KEY_ATTENDANT_ON
    "XF86AttendantOff":		0x1008121c,		# v3.10 KEY_ATTENDANT_OFF
    "XF86AttendantToggle":		0x1008121d,		# v3.10 KEY_ATTENDANT_TOGGLE
    "XF86LightsToggle":		0x1008121e,		# v3.10 KEY_LIGHTS_TOGGLE
    "XF86ALSToggle":		0x10081230,		# v3.13 KEY_ALS_TOGGLE
    "XF86Buttonconfig":		0x10081240,		# v3.16 KEY_BUTTONCONFIG
    "XF86Taskmanager":		0x10081241,		# v3.16 KEY_TASKMANAGER
    "XF86Journal":			0x10081242,		# v3.16 KEY_JOURNAL
    "XF86ControlPanel":		0x10081243,		# v3.16 KEY_CONTROLPANEL
    "XF86AppSelect":		0x10081244,		# v3.16 KEY_APPSELECT
    "XF86Screensaver":		0x10081245,		# v3.16 KEY_SCREENSAVER
    "XF86VoiceCommand":		0x10081246,		# v3.16 KEY_VOICECOMMAND
    "XF86Assistant":		0x10081247,		# v4.13 KEY_ASSISTANT
    "XF86EmojiPicker":		0x10081249,		# v5.13 KEY_EMOJI_PICKER
    "XF86Dictate":			0x1008124a,		# v5.17 KEY_DICTATE
    "XF86BrightnessMin":		0x10081250,		# v3.16 KEY_BRIGHTNESS_MIN
    "XF86BrightnessMax":		0x10081251,		# v3.16 KEY_BRIGHTNESS_MAX
    "XF86KbdInputAssistPrev":	0x10081260,		# v3.18 KEY_KBDINPUTASSIST_PREV
    "XF86KbdInputAssistNext":	0x10081261,		# v3.18 KEY_KBDINPUTASSIST_NEXT
    "XF86KbdInputAssistPrevgroup":	0x10081262,		# v3.18 KEY_KBDINPUTASSIST_PREVGROUP
    "XF86KbdInputAssistNextgroup":	0x10081263,		# v3.18 KEY_KBDINPUTASSIST_NEXTGROUP
    "XF86KbdInputAssistAccept":	0x10081264,		# v3.18 KEY_KBDINPUTASSIST_ACCEPT
    "XF86KbdInputAssistCancel":	0x10081265,		# v3.18 KEY_KBDINPUTASSIST_CANCEL
    "XF86RightUp":			0x10081266,		# v4.7  KEY_RIGHT_UP
    "XF86RightDown":		0x10081267,		# v4.7  KEY_RIGHT_DOWN
    "XF86LeftUp":			0x10081268,		# v4.7  KEY_LEFT_UP
    "XF86LeftDown":			0x10081269,		# v4.7  KEY_LEFT_DOWN
    "XF86RootMenu":			0x1008126a,		# v4.7  KEY_ROOT_MENU
    "XF86MediaTopMenu":		0x1008126b,		# v4.7  KEY_MEDIA_TOP_MENU
    "XF86Numeric11":		0x1008126c,		# v4.7  KEY_NUMERIC_11
    "XF86Numeric12":		0x1008126d,		# v4.7  KEY_NUMERIC_12
    "XF86AudioDesc":		0x1008126e,		# v4.7  KEY_AUDIO_DESC
    "XF863DMode":			0x1008126f,		# v4.7  KEY_3D_MODE
    "XF86NextFavorite":		0x10081270,		# v4.7  KEY_NEXT_FAVORITE
    "XF86StopRecord":		0x10081271,		# v4.7  KEY_STOP_RECORD
    "XF86PauseRecord":		0x10081272,		# v4.7  KEY_PAUSE_RECORD
    "XF86VOD":			0x10081273,		# v4.7  KEY_VOD
    "XF86Unmute":			0x10081274,		# v4.7  KEY_UNMUTE
    "XF86FastReverse":		0x10081275,		# v4.7  KEY_FASTREVERSE
    "XF86SlowReverse":		0x10081276,		# v4.7  KEY_SLOWREVERSE
    "XF86Data":			0x10081277,		# v4.7  KEY_DATA
    "XF86OnScreenKeyboard":		0x10081278,		# v4.12 KEY_ONSCREEN_KEYBOARD
    "XF86PrivacyScreenToggle":	0x10081279,		# v5.5  KEY_PRIVACY_SCREEN_TOGGLE
    "XF86SelectiveScreenshot":	0x1008127a,		# v5.6  KEY_SELECTIVE_SCREENSHOT
    "XF86Macro1":			0x10081290,		# v5.5  KEY_MACRO1
    "XF86Macro2":			0x10081291,		# v5.5  KEY_MACRO2
    "XF86Macro3":			0x10081292,		# v5.5  KEY_MACRO3
    "XF86Macro4":			0x10081293,		# v5.5  KEY_MACRO4
    "XF86Macro5":			0x10081294,		# v5.5  KEY_MACRO5
    "XF86Macro6":			0x10081295,		# v5.5  KEY_MACRO6
    "XF86Macro7":			0x10081296,		# v5.5  KEY_MACRO7
    "XF86Macro8":			0x10081297,		# v5.5  KEY_MACRO8
    "XF86Macro9":			0x10081298,		# v5.5  KEY_MACRO9
    "XF86Macro10":			0x10081299,		# v5.5  KEY_MACRO10
    "XF86Macro11":			0x1008129a,		# v5.5  KEY_MACRO11
    "XF86Macro12":			0x1008129b,		# v5.5  KEY_MACRO12
    "XF86Macro13":			0x1008129c,		# v5.5  KEY_MACRO13
    "XF86Macro14":			0x1008129d,		# v5.5  KEY_MACRO14
    "XF86Macro15":			0x1008129e,		# v5.5  KEY_MACRO15
    "XF86Macro16":			0x1008129f,		# v5.5  KEY_MACRO16
    "XF86Macro17":			0x100812a0,		# v5.5  KEY_MACRO17
    "XF86Macro18":			0x100812a1,		# v5.5  KEY_MACRO18
    "XF86Macro19":			0x100812a2,		# v5.5  KEY_MACRO19
    "XF86Macro20":			0x100812a3,		# v5.5  KEY_MACRO20
    "XF86Macro21":			0x100812a4,		# v5.5  KEY_MACRO21
    "XF86Macro22":			0x100812a5,		# v5.5  KEY_MACRO22
    "XF86Macro23":			0x100812a6,		# v5.5  KEY_MACRO23
    "XF86Macro24":			0x100812a7,		# v5.5  KEY_MACRO24
    "XF86Macro25":			0x100812a8,		# v5.5  KEY_MACRO25
    "XF86Macro26":			0x100812a9,		# v5.5  KEY_MACRO26
    "XF86Macro27":			0x100812aa,		# v5.5  KEY_MACRO27
    "XF86Macro28":			0x100812ab,		# v5.5  KEY_MACRO28
    "XF86Macro29":			0x100812ac,		# v5.5  KEY_MACRO29
    "XF86Macro30":			0x100812ad,		# v5.5  KEY_MACRO30
    "XF86MacroRecordStart":		0x100812b0,		# v5.5  KEY_MACRO_RECORD_START
    "XF86MacroRecordStop":		0x100812b1,		# v5.5  KEY_MACRO_RECORD_STOP
    "XF86MacroPresetCycle":		0x100812b2,		# v5.5  KEY_MACRO_PRESET_CYCLE
    "XF86MacroPreset1":		0x100812b3,		# v5.5  KEY_MACRO_PRESET1
    "XF86MacroPreset2":		0x100812b4,		# v5.5  KEY_MACRO_PRESET2
    "XF86MacroPreset3":		0x100812b5,		# v5.5  KEY_MACRO_PRESET3
    "XF86KbdLcdMenu1":		0x100812b8,		# v5.5  KEY_KBD_LCD_MENU1
    "XF86KbdLcdMenu2":		0x100812b9,		# v5.5  KEY_KBD_LCD_MENU2
    "XF86KbdLcdMenu3":		0x100812ba,		# v5.5  KEY_KBD_LCD_MENU3
    "XF86KbdLcdMenu4":		0x100812bb,		# v5.5  KEY_KBD_LCD_MENU4
    "XF86KbdLcdMenu5":		0x100812bc,		# v5.5  KEY_KBD_LCD_MENU5
    "SunFA_Grave":		0x1005FF00,
    "SunFA_Circum":		0x1005FF01,
    "SunFA_Tilde":		0x1005FF02,
    "SunFA_Acute":		0x1005FF03,
    "SunFA_Diaeresis":	0x1005FF04,
    "SunFA_Cedilla":	0x1005FF05,
    "SunF36":		0x1005FF10,	# Labeled F11
    "SunF37":		0x1005FF11,	# Labeled F12
    "SunSys_Req":   	0x1005FF60,
    "SunPrint_Screen":	0x0000FF61,	# Same as XK_Print
    "SunCompose":		0x0000FF20,	# Same as XK_Multi_key
    "SunAltGraph":		0x0000FF7E,	# Same as XK_Mode_switch
    "SunPageUp":		0x0000FF55, 	# Same as XK_Prior
    "SunPageDown":		0x0000FF56,	# Same as XK_Next
    "SunUndo":		0x0000FF65,	# Same as XK_Undo
    "SunAgain":		0x0000FF66,	# Same as XK_Redo
    "SunFind":		0x0000FF68,	# Same as XK_Find
    "SunStop":		0x0000FF69,	# Same as XK_Cancel
    "SunProps":		0x1005FF70,
    "SunFront":		0x1005FF71,
    "SunCopy":		0x1005FF72,
    "SunOpen":		0x1005FF73,
    "SunPaste":		0x1005FF74,
    "SunCut":		0x1005FF75,
    "SunPowerSwitch":		0x1005FF76,
    "SunAudioLowerVolume":		0x1005FF77,
    "SunAudioMute":			0x1005FF78,
    "SunAudioRaiseVolume":		0x1005FF79,
    "SunVideoDegauss":		0x1005FF7A,
    "SunVideoLowerBrightness":	0x1005FF7B,
    "SunVideoRaiseBrightness":	0x1005FF7C,
    "SunPowerSwitchShift":		0x1005FF7D,
    "Dring_accent":         0x1000FEB0,
    "Dcircumflex_accent":   0x1000FE5E,
    "Dcedilla_accent":      0x1000FE2C,
    "Dacute_accent":        0x1000FE27,
    "Dgrave_accent":        0x1000FE60,
    "Dtilde":               0x1000FE7E,
    "Ddiaeresis":           0x1000FE22,
    "DRemove":	0x1000FF00,   # Remove
    "hpClearLine":		0x1000FF6F,
    "hpInsertLine":		0x1000FF70,
    "hpDeleteLine":		0x1000FF71,
    "hpInsertChar":		0x1000FF72,
    "hpDeleteChar":		0x1000FF73,
    "hpBackTab":		0x1000FF74,
    "hpKP_BackTab":		0x1000FF75,
    "hpModelock1":		0x1000FF48,
    "hpModelock2":		0x1000FF49,
    "hpReset":		0x1000FF6C,
    "hpSystem":		0x1000FF6D,
    "hpUser":		0x1000FF6E,
    "hpmute_acute":		0x100000A8,
    "hpmute_grave":		0x100000A9,
    "hpmute_asciicircum":	0x100000AA,
    "hpmute_diaeresis":	0x100000AB,
    "hpmute_asciitilde":	0x100000AC,
    "hplira":		0x100000AF,
    "hpguilder":		0x100000BE,
    "hpYdiaeresis":		0x100000EE,
    "hpIO":			0x100000EE,
    "hplongminus":		0x100000F6,
    "hpblock":		0x100000FC,
    "osfCopy":		0x1004FF02,
    "osfCut":		0x1004FF03,
    "osfPaste":		0x1004FF04,
    "osfBackTab":		0x1004FF07,
    "osfBackSpace":		0x1004FF08,
    "osfClear":		0x1004FF0B,
    "osfEscape":		0x1004FF1B,
    "osfAddMode":		0x1004FF31,
    "osfPrimaryPaste":	0x1004FF32,
    "osfQuickPaste":	0x1004FF33,
    "osfPageLeft":		0x1004FF40,
    "osfPageUp":		0x1004FF41,
    "osfPageDown":		0x1004FF42,
    "osfPageRight":		0x1004FF43,
    "osfActivate":		0x1004FF44,
    "osfMenuBar":		0x1004FF45,
    "osfLeft":		0x1004FF51,
    "osfUp":		0x1004FF52,
    "osfRight":		0x1004FF53,
    "osfDown":		0x1004FF54,
    "osfEndLine":		0x1004FF57,
    "osfBeginLine":		0x1004FF58,
    "osfEndData":		0x1004FF59,
    "osfBeginData":		0x1004FF5A,
    "osfPrevMenu":		0x1004FF5B,
    "osfNextMenu":		0x1004FF5C,
    "osfPrevField":		0x1004FF5D,
    "osfNextField":		0x1004FF5E,
    "osfSelect":		0x1004FF60,
    "osfInsert":		0x1004FF63,
    "osfUndo":		0x1004FF65,
    "osfMenu":		0x1004FF67,
    "osfCancel":		0x1004FF69,
    "osfHelp":		0x1004FF6A,
    "osfSelectAll":		0x1004FF71,
    "osfDeselectAll":	0x1004FF72,
    "osfReselect":		0x1004FF73,
    "osfExtend":		0x1004FF74,
    "osfRestore":		0x1004FF78,
    "osfDelete":		0x1004FFFF,
    "Reset":                0x1000FF6C,
    "System":               0x1000FF6D,
    "User":                 0x1000FF6E,
    "ClearLine":            0x1000FF6F,
    "InsertLine":           0x1000FF70,
    "DeleteLine":           0x1000FF71,
    "InsertChar":           0x1000FF72,
    "DeleteChar":           0x1000FF73,
    "BackTab":              0x1000FF74,
    "KP_BackTab":           0x1000FF75,
    "Ext16bit_L":           0x1000FF76,
    "Ext16bit_R":           0x1000FF77,
    "mute_acute":           0x100000a8,
    "mute_grave":           0x100000a9,
    "mute_asciicircum":     0x100000aa,
    "mute_diaeresis":       0x100000ab,
    "mute_asciitilde":      0x100000ac,
    "lira":                 0x100000af,
    "guilder":              0x100000be,
    "IO":                   0x100000ee,
    "longminus":            0x100000f6,
    "block":                0x100000fc,
}

keysymtab = {
    0x01a1: 0x0104, #                     Aogonek Ą LATIN CAPITAL LETTER A WITH OGONEK
    0x01a2: 0x02d8, #                       breve ˘ BREVE
    0x01a3: 0x0141, #                     Lstroke Ł LATIN CAPITAL LETTER L WITH STROKE
    0x01a5: 0x013d, #                      Lcaron Ľ LATIN CAPITAL LETTER L WITH CARON
    0x01a6: 0x015a, #                      Sacute Ś LATIN CAPITAL LETTER S WITH ACUTE
    0x01a9: 0x0160, #                      Scaron Š LATIN CAPITAL LETTER S WITH CARON
    0x01aa: 0x015e, #                    Scedilla Ş LATIN CAPITAL LETTER S WITH CEDILLA
    0x01ab: 0x0164, #                      Tcaron Ť LATIN CAPITAL LETTER T WITH CARON
    0x01ac: 0x0179, #                      Zacute Ź LATIN CAPITAL LETTER Z WITH ACUTE
    0x01ae: 0x017d, #                      Zcaron Ž LATIN CAPITAL LETTER Z WITH CARON
    0x01af: 0x017b, #                   Zabovedot Ż LATIN CAPITAL LETTER Z WITH DOT ABOVE
    0x01b1: 0x0105, #                     aogonek ą LATIN SMALL LETTER A WITH OGONEK
    0x01b2: 0x02db, #                      ogonek ˛ OGONEK
    0x01b3: 0x0142, #                     lstroke ł LATIN SMALL LETTER L WITH STROKE
    0x01b5: 0x013e, #                      lcaron ľ LATIN SMALL LETTER L WITH CARON
    0x01b6: 0x015b, #                      sacute ś LATIN SMALL LETTER S WITH ACUTE
    0x01b7: 0x02c7, #                       caron ˇ CARON
    0x01b9: 0x0161, #                      scaron š LATIN SMALL LETTER S WITH CARON
    0x01ba: 0x015f, #                    scedilla ş LATIN SMALL LETTER S WITH CEDILLA
    0x01bb: 0x0165, #                      tcaron ť LATIN SMALL LETTER T WITH CARON
    0x01bc: 0x017a, #                      zacute ź LATIN SMALL LETTER Z WITH ACUTE
    0x01bd: 0x02dd, #                 doubleacute ˝ DOUBLE ACUTE ACCENT
    0x01be: 0x017e, #                      zcaron ž LATIN SMALL LETTER Z WITH CARON
    0x01bf: 0x017c, #                   zabovedot ż LATIN SMALL LETTER Z WITH DOT ABOVE
    0x01c0: 0x0154, #                      Racute Ŕ LATIN CAPITAL LETTER R WITH ACUTE
    0x01c3: 0x0102, #                      Abreve Ă LATIN CAPITAL LETTER A WITH BREVE
    0x01c5: 0x0139, #                      Lacute Ĺ LATIN CAPITAL LETTER L WITH ACUTE
    0x01c6: 0x0106, #                      Cacute Ć LATIN CAPITAL LETTER C WITH ACUTE
    0x01c8: 0x010c, #                      Ccaron Č LATIN CAPITAL LETTER C WITH CARON
    0x01ca: 0x0118, #                     Eogonek Ę LATIN CAPITAL LETTER E WITH OGONEK
    0x01cc: 0x011a, #                      Ecaron Ě LATIN CAPITAL LETTER E WITH CARON
    0x01cf: 0x010e, #                      Dcaron Ď LATIN CAPITAL LETTER D WITH CARON
    0x01d0: 0x0110, #                     Dstroke Đ LATIN CAPITAL LETTER D WITH STROKE
    0x01d1: 0x0143, #                      Nacute Ń LATIN CAPITAL LETTER N WITH ACUTE
    0x01d2: 0x0147, #                      Ncaron Ň LATIN CAPITAL LETTER N WITH CARON
    0x01d5: 0x0150, #                Odoubleacute Ő LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
    0x01d8: 0x0158, #                      Rcaron Ř LATIN CAPITAL LETTER R WITH CARON
    0x01d9: 0x016e, #                       Uring Ů LATIN CAPITAL LETTER U WITH RING ABOVE
    0x01db: 0x0170, #                Udoubleacute Ű LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
    0x01de: 0x0162, #                    Tcedilla Ţ LATIN CAPITAL LETTER T WITH CEDILLA
    0x01e0: 0x0155, #                      racute ŕ LATIN SMALL LETTER R WITH ACUTE
    0x01e3: 0x0103, #                      abreve ă LATIN SMALL LETTER A WITH BREVE
    0x01e5: 0x013a, #                      lacute ĺ LATIN SMALL LETTER L WITH ACUTE
    0x01e6: 0x0107, #                      cacute ć LATIN SMALL LETTER C WITH ACUTE
    0x01e8: 0x010d, #                      ccaron č LATIN SMALL LETTER C WITH CARON
    0x01ea: 0x0119, #                     eogonek ę LATIN SMALL LETTER E WITH OGONEK
    0x01ec: 0x011b, #                      ecaron ě LATIN SMALL LETTER E WITH CARON
    0x01ef: 0x010f, #                      dcaron ď LATIN SMALL LETTER D WITH CARON
    0x01f0: 0x0111, #                     dstroke đ LATIN SMALL LETTER D WITH STROKE
    0x01f1: 0x0144, #                      nacute ń LATIN SMALL LETTER N WITH ACUTE
    0x01f2: 0x0148, #                      ncaron ň LATIN SMALL LETTER N WITH CARON
    0x01f5: 0x0151, #                odoubleacute ő LATIN SMALL LETTER O WITH DOUBLE ACUTE
    0x01f8: 0x0159, #                      rcaron ř LATIN SMALL LETTER R WITH CARON
    0x01f9: 0x016f, #                       uring ů LATIN SMALL LETTER U WITH RING ABOVE
    0x01fb: 0x0171, #                udoubleacute ű LATIN SMALL LETTER U WITH DOUBLE ACUTE
    0x01fe: 0x0163, #                    tcedilla ţ LATIN SMALL LETTER T WITH CEDILLA
    0x01ff: 0x02d9, #                    abovedot ˙ DOT ABOVE
    0x02a1: 0x0126, #                     Hstroke Ħ LATIN CAPITAL LETTER H WITH STROKE
    0x02a6: 0x0124, #                 Hcircumflex Ĥ LATIN CAPITAL LETTER H WITH CIRCUMFLEX
    0x02a9: 0x0130, #                   Iabovedot İ LATIN CAPITAL LETTER I WITH DOT ABOVE
    0x02ab: 0x011e, #                      Gbreve Ğ LATIN CAPITAL LETTER G WITH BREVE
    0x02ac: 0x0134, #                 Jcircumflex Ĵ LATIN CAPITAL LETTER J WITH CIRCUMFLEX
    0x02b1: 0x0127, #                     hstroke ħ LATIN SMALL LETTER H WITH STROKE
    0x02b6: 0x0125, #                 hcircumflex ĥ LATIN SMALL LETTER H WITH CIRCUMFLEX
    0x02b9: 0x0131, #                    idotless ı LATIN SMALL LETTER DOTLESS I
    0x02bb: 0x011f, #                      gbreve ğ LATIN SMALL LETTER G WITH BREVE
    0x02bc: 0x0135, #                 jcircumflex ĵ LATIN SMALL LETTER J WITH CIRCUMFLEX
    0x02c5: 0x010a, #                   Cabovedot Ċ LATIN CAPITAL LETTER C WITH DOT ABOVE
    0x02c6: 0x0108, #                 Ccircumflex Ĉ LATIN CAPITAL LETTER C WITH CIRCUMFLEX
    0x02d5: 0x0120, #                   Gabovedot Ġ LATIN CAPITAL LETTER G WITH DOT ABOVE
    0x02d8: 0x011c, #                 Gcircumflex Ĝ LATIN CAPITAL LETTER G WITH CIRCUMFLEX
    0x02dd: 0x016c, #                      Ubreve Ŭ LATIN CAPITAL LETTER U WITH BREVE
    0x02de: 0x015c, #                 Scircumflex Ŝ LATIN CAPITAL LETTER S WITH CIRCUMFLEX
    0x02e5: 0x010b, #                   cabovedot ċ LATIN SMALL LETTER C WITH DOT ABOVE
    0x02e6: 0x0109, #                 ccircumflex ĉ LATIN SMALL LETTER C WITH CIRCUMFLEX
    0x02f5: 0x0121, #                   gabovedot ġ LATIN SMALL LETTER G WITH DOT ABOVE
    0x02f8: 0x011d, #                 gcircumflex ĝ LATIN SMALL LETTER G WITH CIRCUMFLEX
    0x02fd: 0x016d, #                      ubreve ŭ LATIN SMALL LETTER U WITH BREVE
    0x02fe: 0x015d, #                 scircumflex ŝ LATIN SMALL LETTER S WITH CIRCUMFLEX
    0x03a2: 0x0138, #                         kra ĸ LATIN SMALL LETTER KRA
    0x03a3: 0x0156, #                    Rcedilla Ŗ LATIN CAPITAL LETTER R WITH CEDILLA
    0x03a5: 0x0128, #                      Itilde Ĩ LATIN CAPITAL LETTER I WITH TILDE
    0x03a6: 0x013b, #                    Lcedilla Ļ LATIN CAPITAL LETTER L WITH CEDILLA
    0x03aa: 0x0112, #                     Emacron Ē LATIN CAPITAL LETTER E WITH MACRON
    0x03ab: 0x0122, #                    Gcedilla Ģ LATIN CAPITAL LETTER G WITH CEDILLA
    0x03ac: 0x0166, #                      Tslash Ŧ LATIN CAPITAL LETTER T WITH STROKE
    0x03b3: 0x0157, #                    rcedilla ŗ LATIN SMALL LETTER R WITH CEDILLA
    0x03b5: 0x0129, #                      itilde ĩ LATIN SMALL LETTER I WITH TILDE
    0x03b6: 0x013c, #                    lcedilla ļ LATIN SMALL LETTER L WITH CEDILLA
    0x03ba: 0x0113, #                     emacron ē LATIN SMALL LETTER E WITH MACRON
    0x03bb: 0x0123, #                    gcedilla ģ LATIN SMALL LETTER G WITH CEDILLA
    0x03bc: 0x0167, #                      tslash ŧ LATIN SMALL LETTER T WITH STROKE
    0x03bd: 0x014a, #                         ENG Ŋ LATIN CAPITAL LETTER ENG
    0x03bf: 0x014b, #                         eng ŋ LATIN SMALL LETTER ENG
    0x03c0: 0x0100, #                     Amacron Ā LATIN CAPITAL LETTER A WITH MACRON
    0x03c7: 0x012e, #                     Iogonek Į LATIN CAPITAL LETTER I WITH OGONEK
    0x03cc: 0x0116, #                   Eabovedot Ė LATIN CAPITAL LETTER E WITH DOT ABOVE
    0x03cf: 0x012a, #                     Imacron Ī LATIN CAPITAL LETTER I WITH MACRON
    0x03d1: 0x0145, #                    Ncedilla Ņ LATIN CAPITAL LETTER N WITH CEDILLA
    0x03d2: 0x014c, #                     Omacron Ō LATIN CAPITAL LETTER O WITH MACRON
    0x03d3: 0x0136, #                    Kcedilla Ķ LATIN CAPITAL LETTER K WITH CEDILLA
    0x03d9: 0x0172, #                     Uogonek Ų LATIN CAPITAL LETTER U WITH OGONEK
    0x03dd: 0x0168, #                      Utilde Ũ LATIN CAPITAL LETTER U WITH TILDE
    0x03de: 0x016a, #                     Umacron Ū LATIN CAPITAL LETTER U WITH MACRON
    0x03e0: 0x0101, #                     amacron ā LATIN SMALL LETTER A WITH MACRON
    0x03e7: 0x012f, #                     iogonek į LATIN SMALL LETTER I WITH OGONEK
    0x03ec: 0x0117, #                   eabovedot ė LATIN SMALL LETTER E WITH DOT ABOVE
    0x03ef: 0x012b, #                     imacron ī LATIN SMALL LETTER I WITH MACRON
    0x03f1: 0x0146, #                    ncedilla ņ LATIN SMALL LETTER N WITH CEDILLA
    0x03f2: 0x014d, #                     omacron ō LATIN SMALL LETTER O WITH MACRON
    0x03f3: 0x0137, #                    kcedilla ķ LATIN SMALL LETTER K WITH CEDILLA
    0x03f9: 0x0173, #                     uogonek ų LATIN SMALL LETTER U WITH OGONEK
    0x03fd: 0x0169, #                      utilde ũ LATIN SMALL LETTER U WITH TILDE
    0x03fe: 0x016b, #                     umacron ū LATIN SMALL LETTER U WITH MACRON
    0x047e: 0x203e, #                    overline ‾ OVERLINE
    0x04a1: 0x3002, #               kana_fullstop 。 IDEOGRAPHIC FULL STOP
    0x04a2: 0x300c, #         kana_openingbracket 「 LEFT CORNER BRACKET
    0x04a3: 0x300d, #         kana_closingbracket 」 RIGHT CORNER BRACKET
    0x04a4: 0x3001, #                  kana_comma 、 IDEOGRAPHIC COMMA
    0x04a5: 0x30fb, #            kana_conjunctive ・ KATAKANA MIDDLE DOT
    0x04a6: 0x30f2, #                     kana_WO ヲ KATAKANA LETTER WO
    0x04a7: 0x30a1, #                      kana_a ァ KATAKANA LETTER SMALL A
    0x04a8: 0x30a3, #                      kana_i ィ KATAKANA LETTER SMALL I
    0x04a9: 0x30a5, #                      kana_u ゥ KATAKANA LETTER SMALL U
    0x04aa: 0x30a7, #                      kana_e ェ KATAKANA LETTER SMALL E
    0x04ab: 0x30a9, #                      kana_o ォ KATAKANA LETTER SMALL O
    0x04ac: 0x30e3, #                     kana_ya ャ KATAKANA LETTER SMALL YA
    0x04ad: 0x30e5, #                     kana_yu ュ KATAKANA LETTER SMALL YU
    0x04ae: 0x30e7, #                     kana_yo ョ KATAKANA LETTER SMALL YO
    0x04af: 0x30c3, #                    kana_tsu ッ KATAKANA LETTER SMALL TU
    0x04b0: 0x30fc, #              prolongedsound ー KATAKANA-HIRAGANA PROLONGED SOUND MARK
    0x04b1: 0x30a2, #                      kana_A ア KATAKANA LETTER A
    0x04b2: 0x30a4, #                      kana_I イ KATAKANA LETTER I
    0x04b3: 0x30a6, #                      kana_U ウ KATAKANA LETTER U
    0x04b4: 0x30a8, #                      kana_E エ KATAKANA LETTER E
    0x04b5: 0x30aa, #                      kana_O オ KATAKANA LETTER O
    0x04b6: 0x30ab, #                     kana_KA カ KATAKANA LETTER KA
    0x04b7: 0x30ad, #                     kana_KI キ KATAKANA LETTER KI
    0x04b8: 0x30af, #                     kana_KU ク KATAKANA LETTER KU
    0x04b9: 0x30b1, #                     kana_KE ケ KATAKANA LETTER KE
    0x04ba: 0x30b3, #                     kana_KO コ KATAKANA LETTER KO
    0x04bb: 0x30b5, #                     kana_SA サ KATAKANA LETTER SA
    0x04bc: 0x30b7, #                    kana_SHI シ KATAKANA LETTER SI
    0x04bd: 0x30b9, #                     kana_SU ス KATAKANA LETTER SU
    0x04be: 0x30bb, #                     kana_SE セ KATAKANA LETTER SE
    0x04bf: 0x30bd, #                     kana_SO ソ KATAKANA LETTER SO
    0x04c0: 0x30bf, #                     kana_TA タ KATAKANA LETTER TA
    0x04c1: 0x30c1, #                    kana_CHI チ KATAKANA LETTER TI
    0x04c2: 0x30c4, #                    kana_TSU ツ KATAKANA LETTER TU
    0x04c3: 0x30c6, #                     kana_TE テ KATAKANA LETTER TE
    0x04c4: 0x30c8, #                     kana_TO ト KATAKANA LETTER TO
    0x04c5: 0x30ca, #                     kana_NA ナ KATAKANA LETTER NA
    0x04c6: 0x30cb, #                     kana_NI ニ KATAKANA LETTER NI
    0x04c7: 0x30cc, #                     kana_NU ヌ KATAKANA LETTER NU
    0x04c8: 0x30cd, #                     kana_NE ネ KATAKANA LETTER NE
    0x04c9: 0x30ce, #                     kana_NO ノ KATAKANA LETTER NO
    0x04ca: 0x30cf, #                     kana_HA ハ KATAKANA LETTER HA
    0x04cb: 0x30d2, #                     kana_HI ヒ KATAKANA LETTER HI
    0x04cc: 0x30d5, #                     kana_FU フ KATAKANA LETTER HU
    0x04cd: 0x30d8, #                     kana_HE ヘ KATAKANA LETTER HE
    0x04ce: 0x30db, #                     kana_HO ホ KATAKANA LETTER HO
    0x04cf: 0x30de, #                     kana_MA マ KATAKANA LETTER MA
    0x04d0: 0x30df, #                     kana_MI ミ KATAKANA LETTER MI
    0x04d1: 0x30e0, #                     kana_MU ム KATAKANA LETTER MU
    0x04d2: 0x30e1, #                     kana_ME メ KATAKANA LETTER ME
    0x04d3: 0x30e2, #                     kana_MO モ KATAKANA LETTER MO
    0x04d4: 0x30e4, #                     kana_YA ヤ KATAKANA LETTER YA
    0x04d5: 0x30e6, #                     kana_YU ユ KATAKANA LETTER YU
    0x04d6: 0x30e8, #                     kana_YO ヨ KATAKANA LETTER YO
    0x04d7: 0x30e9, #                     kana_RA ラ KATAKANA LETTER RA
    0x04d8: 0x30ea, #                     kana_RI リ KATAKANA LETTER RI
    0x04d9: 0x30eb, #                     kana_RU ル KATAKANA LETTER RU
    0x04da: 0x30ec, #                     kana_RE レ KATAKANA LETTER RE
    0x04db: 0x30ed, #                     kana_RO ロ KATAKANA LETTER RO
    0x04dc: 0x30ef, #                     kana_WA ワ KATAKANA LETTER WA
    0x04dd: 0x30f3, #                      kana_N ン KATAKANA LETTER N
    0x04de: 0x309b, #                 voicedsound ゛ KATAKANA-HIRAGANA VOICED SOUND MARK
    0x04df: 0x309c, #             semivoicedsound ゜ KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK
    0x05ac: 0x060c, #                Arabic_comma ، ARABIC COMMA
    0x05bb: 0x061b, #            Arabic_semicolon ؛ ARABIC SEMICOLON
    0x05bf: 0x061f, #        Arabic_question_mark ؟ ARABIC QUESTION MARK
    0x05c1: 0x0621, #                Arabic_hamza ء ARABIC LETTER HAMZA
    0x05c2: 0x0622, #          Arabic_maddaonalef آ ARABIC LETTER ALEF WITH MADDA ABOVE
    0x05c3: 0x0623, #          Arabic_hamzaonalef أ ARABIC LETTER ALEF WITH HAMZA ABOVE
    0x05c4: 0x0624, #           Arabic_hamzaonwaw ؤ ARABIC LETTER WAW WITH HAMZA ABOVE
    0x05c5: 0x0625, #       Arabic_hamzaunderalef إ ARABIC LETTER ALEF WITH HAMZA BELOW
    0x05c6: 0x0626, #           Arabic_hamzaonyeh ئ ARABIC LETTER YEH WITH HAMZA ABOVE
    0x05c7: 0x0627, #                 Arabic_alef ا ARABIC LETTER ALEF
    0x05c8: 0x0628, #                  Arabic_beh ب ARABIC LETTER BEH
    0x05c9: 0x0629, #           Arabic_tehmarbuta ة ARABIC LETTER TEH MARBUTA
    0x05ca: 0x062a, #                  Arabic_teh ت ARABIC LETTER TEH
    0x05cb: 0x062b, #                 Arabic_theh ث ARABIC LETTER THEH
    0x05cc: 0x062c, #                 Arabic_jeem ج ARABIC LETTER JEEM
    0x05cd: 0x062d, #                  Arabic_hah ح ARABIC LETTER HAH
    0x05ce: 0x062e, #                 Arabic_khah خ ARABIC LETTER KHAH
    0x05cf: 0x062f, #                  Arabic_dal د ARABIC LETTER DAL
    0x05d0: 0x0630, #                 Arabic_thal ذ ARABIC LETTER THAL
    0x05d1: 0x0631, #                   Arabic_ra ر ARABIC LETTER REH
    0x05d2: 0x0632, #                 Arabic_zain ز ARABIC LETTER ZAIN
    0x05d3: 0x0633, #                 Arabic_seen س ARABIC LETTER SEEN
    0x05d4: 0x0634, #                Arabic_sheen ش ARABIC LETTER SHEEN
    0x05d5: 0x0635, #                  Arabic_sad ص ARABIC LETTER SAD
    0x05d6: 0x0636, #                  Arabic_dad ض ARABIC LETTER DAD
    0x05d7: 0x0637, #                  Arabic_tah ط ARABIC LETTER TAH
    0x05d8: 0x0638, #                  Arabic_zah ظ ARABIC LETTER ZAH
    0x05d9: 0x0639, #                  Arabic_ain ع ARABIC LETTER AIN
    0x05da: 0x063a, #                Arabic_ghain غ ARABIC LETTER GHAIN
    0x05e0: 0x0640, #              Arabic_tatweel ـ ARABIC TATWEEL
    0x05e1: 0x0641, #                  Arabic_feh ف ARABIC LETTER FEH
    0x05e2: 0x0642, #                  Arabic_qaf ق ARABIC LETTER QAF
    0x05e3: 0x0643, #                  Arabic_kaf ك ARABIC LETTER KAF
    0x05e4: 0x0644, #                  Arabic_lam ل ARABIC LETTER LAM
    0x05e5: 0x0645, #                 Arabic_meem م ARABIC LETTER MEEM
    0x05e6: 0x0646, #                 Arabic_noon ن ARABIC LETTER NOON
    0x05e7: 0x0647, #                   Arabic_ha ه ARABIC LETTER HEH
    0x05e8: 0x0648, #                  Arabic_waw و ARABIC LETTER WAW
    0x05e9: 0x0649, #          Arabic_alefmaksura ى ARABIC LETTER ALEF MAKSURA
    0x05ea: 0x064a, #                  Arabic_yeh ي ARABIC LETTER YEH
    0x05eb: 0x064b, #             Arabic_fathatan ً ARABIC FATHATAN
    0x05ec: 0x064c, #             Arabic_dammatan ٌ ARABIC DAMMATAN
    0x05ed: 0x064d, #             Arabic_kasratan ٍ ARABIC KASRATAN
    0x05ee: 0x064e, #                Arabic_fatha َ ARABIC FATHA
    0x05ef: 0x064f, #                Arabic_damma ُ ARABIC DAMMA
    0x05f0: 0x0650, #                Arabic_kasra ِ ARABIC KASRA
    0x05f1: 0x0651, #               Arabic_shadda ّ ARABIC SHADDA
    0x05f2: 0x0652, #                Arabic_sukun ْ ARABIC SUKUN
    0x06a1: 0x0452, #                 Serbian_dje ђ CYRILLIC SMALL LETTER DJE
    0x06a2: 0x0453, #               Macedonia_gje ѓ CYRILLIC SMALL LETTER GJE
    0x06a3: 0x0451, #                 Cyrillic_io ё CYRILLIC SMALL LETTER IO
    0x06a4: 0x0454, #                Ukrainian_ie є CYRILLIC SMALL LETTER UKRAINIAN IE
    0x06a5: 0x0455, #               Macedonia_dse ѕ CYRILLIC SMALL LETTER DZE
    0x06a6: 0x0456, #                 Ukrainian_i і CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    0x06a7: 0x0457, #                Ukrainian_yi ї CYRILLIC SMALL LETTER YI
    0x06a8: 0x0458, #                 Cyrillic_je ј CYRILLIC SMALL LETTER JE
    0x06a9: 0x0459, #                Cyrillic_lje љ CYRILLIC SMALL LETTER LJE
    0x06aa: 0x045a, #                Cyrillic_nje њ CYRILLIC SMALL LETTER NJE
    0x06ab: 0x045b, #                Serbian_tshe ћ CYRILLIC SMALL LETTER TSHE
    0x06ac: 0x045c, #               Macedonia_kje ќ CYRILLIC SMALL LETTER KJE
    0x06ad: 0x0491, #   Ukrainian_ghe_with_upturn ґ CYRILLIC SMALL LETTER GHE WITH UPTURN
    0x06ae: 0x045e, #         Byelorussian_shortu ў CYRILLIC SMALL LETTER SHORT U
    0x06af: 0x045f, #               Cyrillic_dzhe џ CYRILLIC SMALL LETTER DZHE
    0x06b0: 0x2116, #                  numerosign № NUMERO SIGN
    0x06b1: 0x0402, #                 Serbian_DJE Ђ CYRILLIC CAPITAL LETTER DJE
    0x06b2: 0x0403, #               Macedonia_GJE Ѓ CYRILLIC CAPITAL LETTER GJE
    0x06b3: 0x0401, #                 Cyrillic_IO Ё CYRILLIC CAPITAL LETTER IO
    0x06b4: 0x0404, #                Ukrainian_IE Є CYRILLIC CAPITAL LETTER UKRAINIAN IE
    0x06b5: 0x0405, #               Macedonia_DSE Ѕ CYRILLIC CAPITAL LETTER DZE
    0x06b6: 0x0406, #                 Ukrainian_I І CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    0x06b7: 0x0407, #                Ukrainian_YI Ї CYRILLIC CAPITAL LETTER YI
    0x06b8: 0x0408, #                 Cyrillic_JE Ј CYRILLIC CAPITAL LETTER JE
    0x06b9: 0x0409, #                Cyrillic_LJE Љ CYRILLIC CAPITAL LETTER LJE
    0x06ba: 0x040a, #                Cyrillic_NJE Њ CYRILLIC CAPITAL LETTER NJE
    0x06bb: 0x040b, #                Serbian_TSHE Ћ CYRILLIC CAPITAL LETTER TSHE
    0x06bc: 0x040c, #               Macedonia_KJE Ќ CYRILLIC CAPITAL LETTER KJE
    0x06bd: 0x0490, #   Ukrainian_GHE_WITH_UPTURN Ґ CYRILLIC CAPITAL LETTER GHE WITH UPTURN
    0x06be: 0x040e, #         Byelorussian_SHORTU Ў CYRILLIC CAPITAL LETTER SHORT U
    0x06bf: 0x040f, #               Cyrillic_DZHE Џ CYRILLIC CAPITAL LETTER DZHE
    0x06c0: 0x044e, #                 Cyrillic_yu ю CYRILLIC SMALL LETTER YU
    0x06c1: 0x0430, #                  Cyrillic_a а CYRILLIC SMALL LETTER A
    0x06c2: 0x0431, #                 Cyrillic_be б CYRILLIC SMALL LETTER BE
    0x06c3: 0x0446, #                Cyrillic_tse ц CYRILLIC SMALL LETTER TSE
    0x06c4: 0x0434, #                 Cyrillic_de д CYRILLIC SMALL LETTER DE
    0x06c5: 0x0435, #                 Cyrillic_ie е CYRILLIC SMALL LETTER IE
    0x06c6: 0x0444, #                 Cyrillic_ef ф CYRILLIC SMALL LETTER EF
    0x06c7: 0x0433, #                Cyrillic_ghe г CYRILLIC SMALL LETTER GHE
    0x06c8: 0x0445, #                 Cyrillic_ha х CYRILLIC SMALL LETTER HA
    0x06c9: 0x0438, #                  Cyrillic_i и CYRILLIC SMALL LETTER I
    0x06ca: 0x0439, #             Cyrillic_shorti й CYRILLIC SMALL LETTER SHORT I
    0x06cb: 0x043a, #                 Cyrillic_ka к CYRILLIC SMALL LETTER KA
    0x06cc: 0x043b, #                 Cyrillic_el л CYRILLIC SMALL LETTER EL
    0x06cd: 0x043c, #                 Cyrillic_em м CYRILLIC SMALL LETTER EM
    0x06ce: 0x043d, #                 Cyrillic_en н CYRILLIC SMALL LETTER EN
    0x06cf: 0x043e, #                  Cyrillic_o о CYRILLIC SMALL LETTER O
    0x06d0: 0x043f, #                 Cyrillic_pe п CYRILLIC SMALL LETTER PE
    0x06d1: 0x044f, #                 Cyrillic_ya я CYRILLIC SMALL LETTER YA
    0x06d2: 0x0440, #                 Cyrillic_er р CYRILLIC SMALL LETTER ER
    0x06d3: 0x0441, #                 Cyrillic_es с CYRILLIC SMALL LETTER ES
    0x06d4: 0x0442, #                 Cyrillic_te т CYRILLIC SMALL LETTER TE
    0x06d5: 0x0443, #                  Cyrillic_u у CYRILLIC SMALL LETTER U
    0x06d6: 0x0436, #                Cyrillic_zhe ж CYRILLIC SMALL LETTER ZHE
    0x06d7: 0x0432, #                 Cyrillic_ve в CYRILLIC SMALL LETTER VE
    0x06d8: 0x044c, #           Cyrillic_softsign ь CYRILLIC SMALL LETTER SOFT SIGN
    0x06d9: 0x044b, #               Cyrillic_yeru ы CYRILLIC SMALL LETTER YERU
    0x06da: 0x0437, #                 Cyrillic_ze з CYRILLIC SMALL LETTER ZE
    0x06db: 0x0448, #                Cyrillic_sha ш CYRILLIC SMALL LETTER SHA
    0x06dc: 0x044d, #                  Cyrillic_e э CYRILLIC SMALL LETTER E
    0x06dd: 0x0449, #              Cyrillic_shcha щ CYRILLIC SMALL LETTER SHCHA
    0x06de: 0x0447, #                Cyrillic_che ч CYRILLIC SMALL LETTER CHE
    0x06df: 0x044a, #           Cyrillic_hardsign ъ CYRILLIC SMALL LETTER HARD SIGN
    0x06e0: 0x042e, #                 Cyrillic_YU Ю CYRILLIC CAPITAL LETTER YU
    0x06e1: 0x0410, #                  Cyrillic_A А CYRILLIC CAPITAL LETTER A
    0x06e2: 0x0411, #                 Cyrillic_BE Б CYRILLIC CAPITAL LETTER BE
    0x06e3: 0x0426, #                Cyrillic_TSE Ц CYRILLIC CAPITAL LETTER TSE
    0x06e4: 0x0414, #                 Cyrillic_DE Д CYRILLIC CAPITAL LETTER DE
    0x06e5: 0x0415, #                 Cyrillic_IE Е CYRILLIC CAPITAL LETTER IE
    0x06e6: 0x0424, #                 Cyrillic_EF Ф CYRILLIC CAPITAL LETTER EF
    0x06e7: 0x0413, #                Cyrillic_GHE Г CYRILLIC CAPITAL LETTER GHE
    0x06e8: 0x0425, #                 Cyrillic_HA Х CYRILLIC CAPITAL LETTER HA
    0x06e9: 0x0418, #                  Cyrillic_I И CYRILLIC CAPITAL LETTER I
    0x06ea: 0x0419, #             Cyrillic_SHORTI Й CYRILLIC CAPITAL LETTER SHORT I
    0x06eb: 0x041a, #                 Cyrillic_KA К CYRILLIC CAPITAL LETTER KA
    0x06ec: 0x041b, #                 Cyrillic_EL Л CYRILLIC CAPITAL LETTER EL
    0x06ed: 0x041c, #                 Cyrillic_EM М CYRILLIC CAPITAL LETTER EM
    0x06ee: 0x041d, #                 Cyrillic_EN Н CYRILLIC CAPITAL LETTER EN
    0x06ef: 0x041e, #                  Cyrillic_O О CYRILLIC CAPITAL LETTER O
    0x06f0: 0x041f, #                 Cyrillic_PE П CYRILLIC CAPITAL LETTER PE
    0x06f1: 0x042f, #                 Cyrillic_YA Я CYRILLIC CAPITAL LETTER YA
    0x06f2: 0x0420, #                 Cyrillic_ER Р CYRILLIC CAPITAL LETTER ER
    0x06f3: 0x0421, #                 Cyrillic_ES С CYRILLIC CAPITAL LETTER ES
    0x06f4: 0x0422, #                 Cyrillic_TE Т CYRILLIC CAPITAL LETTER TE
    0x06f5: 0x0423, #                  Cyrillic_U У CYRILLIC CAPITAL LETTER U
    0x06f6: 0x0416, #                Cyrillic_ZHE Ж CYRILLIC CAPITAL LETTER ZHE
    0x06f7: 0x0412, #                 Cyrillic_VE В CYRILLIC CAPITAL LETTER VE
    0x06f8: 0x042c, #           Cyrillic_SOFTSIGN Ь CYRILLIC CAPITAL LETTER SOFT SIGN
    0x06f9: 0x042b, #               Cyrillic_YERU Ы CYRILLIC CAPITAL LETTER YERU
    0x06fa: 0x0417, #                 Cyrillic_ZE З CYRILLIC CAPITAL LETTER ZE
    0x06fb: 0x0428, #                Cyrillic_SHA Ш CYRILLIC CAPITAL LETTER SHA
    0x06fc: 0x042d, #                  Cyrillic_E Э CYRILLIC CAPITAL LETTER E
    0x06fd: 0x0429, #              Cyrillic_SHCHA Щ CYRILLIC CAPITAL LETTER SHCHA
    0x06fe: 0x0427, #                Cyrillic_CHE Ч CYRILLIC CAPITAL LETTER CHE
    0x06ff: 0x042a, #           Cyrillic_HARDSIGN Ъ CYRILLIC CAPITAL LETTER HARD SIGN
    0x07a1: 0x0386, #           Greek_ALPHAaccent Ά GREEK CAPITAL LETTER ALPHA WITH TONOS
    0x07a2: 0x0388, #         Greek_EPSILONaccent Έ GREEK CAPITAL LETTER EPSILON WITH TONOS
    0x07a3: 0x0389, #             Greek_ETAaccent Ή GREEK CAPITAL LETTER ETA WITH TONOS
    0x07a4: 0x038a, #            Greek_IOTAaccent Ί GREEK CAPITAL LETTER IOTA WITH TONOS
    0x07a5: 0x03aa, #         Greek_IOTAdiaeresis Ϊ GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
    0x07a7: 0x038c, #         Greek_OMICRONaccent Ό GREEK CAPITAL LETTER OMICRON WITH TONOS
    0x07a8: 0x038e, #         Greek_UPSILONaccent Ύ GREEK CAPITAL LETTER UPSILON WITH TONOS
    0x07a9: 0x03ab, #       Greek_UPSILONdieresis Ϋ GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
    0x07ab: 0x038f, #           Greek_OMEGAaccent Ώ GREEK CAPITAL LETTER OMEGA WITH TONOS
    0x07ae: 0x0385, #        Greek_accentdieresis ΅ GREEK DIALYTIKA TONOS
    0x07af: 0x2015, #              Greek_horizbar ― HORIZONTAL BAR
    0x07b1: 0x03ac, #           Greek_alphaaccent ά GREEK SMALL LETTER ALPHA WITH TONOS
    0x07b2: 0x03ad, #         Greek_epsilonaccent έ GREEK SMALL LETTER EPSILON WITH TONOS
    0x07b3: 0x03ae, #             Greek_etaaccent ή GREEK SMALL LETTER ETA WITH TONOS
    0x07b4: 0x03af, #            Greek_iotaaccent ί GREEK SMALL LETTER IOTA WITH TONOS
    0x07b5: 0x03ca, #          Greek_iotadieresis ϊ GREEK SMALL LETTER IOTA WITH DIALYTIKA
    0x07b6: 0x0390, #    Greek_iotaaccentdieresis ΐ GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
    0x07b7: 0x03cc, #         Greek_omicronaccent ό GREEK SMALL LETTER OMICRON WITH TONOS
    0x07b8: 0x03cd, #         Greek_upsilonaccent ύ GREEK SMALL LETTER UPSILON WITH TONOS
    0x07b9: 0x03cb, #       Greek_upsilondieresis ϋ GREEK SMALL LETTER UPSILON WITH DIALYTIKA
    0x07ba: 0x03b0, # Greek_upsilonaccentdieresis ΰ GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
    0x07bb: 0x03ce, #           Greek_omegaaccent ώ GREEK SMALL LETTER OMEGA WITH TONOS
    0x07c1: 0x0391, #                 Greek_ALPHA Α GREEK CAPITAL LETTER ALPHA
    0x07c2: 0x0392, #                  Greek_BETA Β GREEK CAPITAL LETTER BETA
    0x07c3: 0x0393, #                 Greek_GAMMA Γ GREEK CAPITAL LETTER GAMMA
    0x07c4: 0x0394, #                 Greek_DELTA Δ GREEK CAPITAL LETTER DELTA
    0x07c5: 0x0395, #               Greek_EPSILON Ε GREEK CAPITAL LETTER EPSILON
    0x07c6: 0x0396, #                  Greek_ZETA Ζ GREEK CAPITAL LETTER ZETA
    0x07c7: 0x0397, #                   Greek_ETA Η GREEK CAPITAL LETTER ETA
    0x07c8: 0x0398, #                 Greek_THETA Θ GREEK CAPITAL LETTER THETA
    0x07c9: 0x0399, #                  Greek_IOTA Ι GREEK CAPITAL LETTER IOTA
    0x07ca: 0x039a, #                 Greek_KAPPA Κ GREEK CAPITAL LETTER KAPPA
    0x07cb: 0x039b, #                Greek_LAMBDA Λ GREEK CAPITAL LETTER LAMDA
    0x07cc: 0x039c, #                    Greek_MU Μ GREEK CAPITAL LETTER MU
    0x07cd: 0x039d, #                    Greek_NU Ν GREEK CAPITAL LETTER NU
    0x07ce: 0x039e, #                    Greek_XI Ξ GREEK CAPITAL LETTER XI
    0x07cf: 0x039f, #               Greek_OMICRON Ο GREEK CAPITAL LETTER OMICRON
    0x07d0: 0x03a0, #                    Greek_PI Π GREEK CAPITAL LETTER PI
    0x07d1: 0x03a1, #                   Greek_RHO Ρ GREEK CAPITAL LETTER RHO
    0x07d2: 0x03a3, #                 Greek_SIGMA Σ GREEK CAPITAL LETTER SIGMA
    0x07d4: 0x03a4, #                   Greek_TAU Τ GREEK CAPITAL LETTER TAU
    0x07d5: 0x03a5, #               Greek_UPSILON Υ GREEK CAPITAL LETTER UPSILON
    0x07d6: 0x03a6, #                   Greek_PHI Φ GREEK CAPITAL LETTER PHI
    0x07d7: 0x03a7, #                   Greek_CHI Χ GREEK CAPITAL LETTER CHI
    0x07d8: 0x03a8, #                   Greek_PSI Ψ GREEK CAPITAL LETTER PSI
    0x07d9: 0x03a9, #                 Greek_OMEGA Ω GREEK CAPITAL LETTER OMEGA
    0x07e1: 0x03b1, #                 Greek_alpha α GREEK SMALL LETTER ALPHA
    0x07e2: 0x03b2, #                  Greek_beta β GREEK SMALL LETTER BETA
    0x07e3: 0x03b3, #                 Greek_gamma γ GREEK SMALL LETTER GAMMA
    0x07e4: 0x03b4, #                 Greek_delta δ GREEK SMALL LETTER DELTA
    0x07e5: 0x03b5, #               Greek_epsilon ε GREEK SMALL LETTER EPSILON
    0x07e6: 0x03b6, #                  Greek_zeta ζ GREEK SMALL LETTER ZETA
    0x07e7: 0x03b7, #                   Greek_eta η GREEK SMALL LETTER ETA
    0x07e8: 0x03b8, #                 Greek_theta θ GREEK SMALL LETTER THETA
    0x07e9: 0x03b9, #                  Greek_iota ι GREEK SMALL LETTER IOTA
    0x07ea: 0x03ba, #                 Greek_kappa κ GREEK SMALL LETTER KAPPA
    0x07eb: 0x03bb, #                Greek_lambda λ GREEK SMALL LETTER LAMDA
    0x07ec: 0x03bc, #                    Greek_mu μ GREEK SMALL LETTER MU
    0x07ed: 0x03bd, #                    Greek_nu ν GREEK SMALL LETTER NU
    0x07ee: 0x03be, #                    Greek_xi ξ GREEK SMALL LETTER XI
    0x07ef: 0x03bf, #               Greek_omicron ο GREEK SMALL LETTER OMICRON
    0x07f0: 0x03c0, #                    Greek_pi π GREEK SMALL LETTER PI
    0x07f1: 0x03c1, #                   Greek_rho ρ GREEK SMALL LETTER RHO
    0x07f2: 0x03c3, #                 Greek_sigma σ GREEK SMALL LETTER SIGMA
    0x07f3: 0x03c2, #       Greek_finalsmallsigma ς GREEK SMALL LETTER FINAL SIGMA
    0x07f4: 0x03c4, #                   Greek_tau τ GREEK SMALL LETTER TAU
    0x07f5: 0x03c5, #               Greek_upsilon υ GREEK SMALL LETTER UPSILON
    0x07f6: 0x03c6, #                   Greek_phi φ GREEK SMALL LETTER PHI
    0x07f7: 0x03c7, #                   Greek_chi χ GREEK SMALL LETTER CHI
    0x07f8: 0x03c8, #                   Greek_psi ψ GREEK SMALL LETTER PSI
    0x07f9: 0x03c9, #                 Greek_omega ω GREEK SMALL LETTER OMEGA
    0x08a1: 0x23b7, #                 leftradical ⎷ ???
    0x08a2: 0x250c, #              topleftradical ┌ BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x08a3: 0x2500, #              horizconnector ─ BOX DRAWINGS LIGHT HORIZONTAL
    0x08a4: 0x2320, #                 topintegral ⌠ TOP HALF INTEGRAL
    0x08a5: 0x2321, #                 botintegral ⌡ BOTTOM HALF INTEGRAL
    0x08a6: 0x2502, #               vertconnector │ BOX DRAWINGS LIGHT VERTICAL
    0x08a7: 0x23a1, #            topleftsqbracket ⎡ ???
    0x08a8: 0x23a3, #            botleftsqbracket ⎣ ???
    0x08a9: 0x23a4, #           toprightsqbracket ⎤ ???
    0x08aa: 0x23a6, #           botrightsqbracket ⎦ ???
    0x08ab: 0x239b, #               topleftparens ⎛ ???
    0x08ac: 0x239d, #               botleftparens ⎝ ???
    0x08ad: 0x239e, #              toprightparens ⎞ ???
    0x08ae: 0x23a0, #              botrightparens ⎠ ???
    0x08af: 0x23a8, #        leftmiddlecurlybrace ⎨ ???
    0x08b0: 0x23ac, #       rightmiddlecurlybrace ⎬ ???
    #  0x08b1                        topleftsummation ? ???
    #  0x08b2                        botleftsummation ? ???
    #  0x08b3               topvertsummationconnector ? ???
    #  0x08b4               botvertsummationconnector ? ???
    #  0x08b5                       toprightsummation ? ???
    #  0x08b6                       botrightsummation ? ???
    #  0x08b7                    rightmiddlesummation ? ???
    0x08bc: 0x2264, #               lessthanequal ≤ LESS-THAN OR EQUAL TO
    0x08bd: 0x2260, #                    notequal ≠ NOT EQUAL TO
    0x08be: 0x2265, #            greaterthanequal ≥ GREATER-THAN OR EQUAL TO
    0x08bf: 0x222b, #                    integral ∫ INTEGRAL
    0x08c0: 0x2234, #                   therefore ∴ THEREFORE
    0x08c1: 0x221d, #                   variation ∝ PROPORTIONAL TO
    0x08c2: 0x221e, #                    infinity ∞ INFINITY
    0x08c5: 0x2207, #                       nabla ∇ NABLA
    0x08c8: 0x223c, #                 approximate ∼ TILDE OPERATOR
    0x08c9: 0x2243, #                similarequal ≃ ASYMPTOTICALLY EQUAL TO
    0x08cd: 0x21d4, #                    ifonlyif ⇔ LEFT RIGHT DOUBLE ARROW
    0x08ce: 0x21d2, #                     implies ⇒ RIGHTWARDS DOUBLE ARROW
    0x08cf: 0x2261, #                   identical ≡ IDENTICAL TO
    0x08d6: 0x221a, #                     radical √ SQUARE ROOT
    0x08da: 0x2282, #                  includedin ⊂ SUBSET OF
    0x08db: 0x2283, #                    includes ⊃ SUPERSET OF
    0x08dc: 0x2229, #                intersection ∩ INTERSECTION
    0x08dd: 0x222a, #                       union ∪ UNION
    0x08de: 0x2227, #                  logicaland ∧ LOGICAL AND
    0x08df: 0x2228, #                   logicalor ∨ LOGICAL OR
    0x08ef: 0x2202, #           partialderivative ∂ PARTIAL DIFFERENTIAL
    0x08f6: 0x0192, #                    function ƒ LATIN SMALL LETTER F WITH HOOK
    0x08fb: 0x2190, #                   leftarrow ← LEFTWARDS ARROW
    0x08fc: 0x2191, #                     uparrow ↑ UPWARDS ARROW
    0x08fd: 0x2192, #                  rightarrow → RIGHTWARDS ARROW
    0x08fe: 0x2193, #                   downarrow ↓ DOWNWARDS ARROW
#  0x09df                                     blank ? ???
    0x09e0: 0x25c6, #                soliddiamond ◆ BLACK DIAMOND
    0x09e1: 0x2592, #                checkerboard ▒ MEDIUM SHADE
    0x09e2: 0x2409, #                          ht ␉ SYMBOL FOR HORIZONTAL TABULATION
    0x09e3: 0x240c, #                          ff ␌ SYMBOL FOR FORM FEED
    0x09e4: 0x240d, #                          cr ␍ SYMBOL FOR CARRIAGE RETURN
    0x09e5: 0x240a, #                          lf ␊ SYMBOL FOR LINE FEED
    0x09e8: 0x2424, #                          nl ␤ SYMBOL FOR NEWLINE
    0x09e9: 0x240b, #                          vt ␋ SYMBOL FOR VERTICAL TABULATION
    0x09ea: 0x2518, #              lowrightcorner ┘ BOX DRAWINGS LIGHT UP AND LEFT
    0x09eb: 0x2510, #               uprightcorner ┐ BOX DRAWINGS LIGHT DOWN AND LEFT
    0x09ec: 0x250c, #                upleftcorner ┌ BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x09ed: 0x2514, #               lowleftcorner └ BOX DRAWINGS LIGHT UP AND RIGHT
    0x09ee: 0x253c, #               crossinglines ┼ BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x09ef: 0x23ba, #              horizlinescan1 ⎺ HORIZONTAL SCAN LINE-1 (Unicode 3.2 draft)
    0x09f0: 0x23bb, #              horizlinescan3 ⎻ HORIZONTAL SCAN LINE-3 (Unicode 3.2 draft)
    0x09f1: 0x2500, #              horizlinescan5 ─ BOX DRAWINGS LIGHT HORIZONTAL
    0x09f2: 0x23bc, #              horizlinescan7 ⎼ HORIZONTAL SCAN LINE-7 (Unicode 3.2 draft)
    0x09f3: 0x23bd, #              horizlinescan9 ⎽ HORIZONTAL SCAN LINE-9 (Unicode 3.2 draft)
    0x09f4: 0x251c, #                       leftt ├ BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x09f5: 0x2524, #                      rightt ┤ BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x09f6: 0x2534, #                        bott ┴ BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x09f7: 0x252c, #                        topt ┬ BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x09f8: 0x2502, #                     vertbar │ BOX DRAWINGS LIGHT VERTICAL
    0x0aa1: 0x2003, #                     emspace   EM SPACE
    0x0aa2: 0x2002, #                     enspace   EN SPACE
    0x0aa3: 0x2004, #                    em3space   THREE-PER-EM SPACE
    0x0aa4: 0x2005, #                    em4space   FOUR-PER-EM SPACE
    0x0aa5: 0x2007, #                  digitspace   FIGURE SPACE
    0x0aa6: 0x2008, #                  punctspace   PUNCTUATION SPACE
    0x0aa7: 0x2009, #                   thinspace   THIN SPACE
    0x0aa8: 0x200a, #                   hairspace   HAIR SPACE
    0x0aa9: 0x2014, #                      emdash — EM DASH
    0x0aaa: 0x2013, #                      endash – EN DASH
    0x0aac: 0x2423, #                 signifblank ␣ OPEN BOX
    0x0aae: 0x2026, #                    ellipsis … HORIZONTAL ELLIPSIS
    0x0aaf: 0x2025, #             doubbaselinedot ‥ TWO DOT LEADER
    0x0ab0: 0x2153, #                    onethird ⅓ VULGAR FRACTION ONE THIRD
    0x0ab1: 0x2154, #                   twothirds ⅔ VULGAR FRACTION TWO THIRDS
    0x0ab2: 0x2155, #                    onefifth ⅕ VULGAR FRACTION ONE FIFTH
    0x0ab3: 0x2156, #                   twofifths ⅖ VULGAR FRACTION TWO FIFTHS
    0x0ab4: 0x2157, #                 threefifths ⅗ VULGAR FRACTION THREE FIFTHS
    0x0ab5: 0x2158, #                  fourfifths ⅘ VULGAR FRACTION FOUR FIFTHS
    0x0ab6: 0x2159, #                    onesixth ⅙ VULGAR FRACTION ONE SIXTH
    0x0ab7: 0x215a, #                  fivesixths ⅚ VULGAR FRACTION FIVE SIXTHS
    0x0ab8: 0x2105, #                      careof ℅ CARE OF
    0x0abb: 0x2012, #                     figdash ‒ FIGURE DASH
    0x0abc: 0x27e8, #            leftanglebracket ⟨ MATHEMATICAL LEFT ANGLE BRACKET
    0x0abd: 0x002e, #                decimalpoint . FULL STOP
    0x0abe: 0x27e9, #           rightanglebracket ⟩ MATHEMATICAL RIGHT ANGLE BRACKET
    #  0x0abf                                  marker ? ???
    0x0ac3: 0x215b, #                   oneeighth ⅛ VULGAR FRACTION ONE EIGHTH
    0x0ac4: 0x215c, #                threeeighths ⅜ VULGAR FRACTION THREE EIGHTHS
    0x0ac5: 0x215d, #                 fiveeighths ⅝ VULGAR FRACTION FIVE EIGHTHS
    0x0ac6: 0x215e, #                seveneighths ⅞ VULGAR FRACTION SEVEN EIGHTHS
    0x0ac9: 0x2122, #                   trademark ™ TRADE MARK SIGN
    0x0aca: 0x2613, #               signaturemark ☓ SALTIRE
    #  0x0acb                       trademarkincircle ? ???
    0x0acc: 0x25c1, #            leftopentriangle ◁ WHITE LEFT-POINTING TRIANGLE
    0x0acd: 0x25b7, #           rightopentriangle ▷ WHITE RIGHT-POINTING TRIANGLE
    0x0ace: 0x25cb, #                emopencircle ○ WHITE CIRCLE
    0x0acf: 0x25af, #             emopenrectangle ▯ WHITE VERTICAL RECTANGLE
    0x0ad0: 0x2018, #         leftsinglequotemark ‘ LEFT SINGLE QUOTATION MARK
    0x0ad1: 0x2019, #        rightsinglequotemark ’ RIGHT SINGLE QUOTATION MARK
    0x0ad2: 0x201c, #         leftdoublequotemark “ LEFT DOUBLE QUOTATION MARK
    0x0ad3: 0x201d, #        rightdoublequotemark ” RIGHT DOUBLE QUOTATION MARK
    0x0ad4: 0x211e, #                prescription ℞ PRESCRIPTION TAKE
    0x0ad5: 0x2030, #                    permille ‰ PER MILLE SIGN
    0x0ad6: 0x2032, #                     minutes ′ PRIME
    0x0ad7: 0x2033, #                     seconds ″ DOUBLE PRIME
    0x0ad9: 0x271d, #                  latincross ✝ LATIN CROSS
    #  0x0ada                                hexagram ? ???
    0x0adb: 0x25ac, #            filledrectbullet ▬ BLACK RECTANGLE
    0x0adc: 0x25c0, #         filledlefttribullet ◀ BLACK LEFT-POINTING TRIANGLE
    0x0add: 0x25b6, #        filledrighttribullet ▶ BLACK RIGHT-POINTING TRIANGLE
    0x0ade: 0x25cf, #              emfilledcircle ● BLACK CIRCLE
    0x0adf: 0x25ae, #                emfilledrect ▮ BLACK VERTICAL RECTANGLE
    0x0ae0: 0x25e6, #            enopencircbullet ◦ WHITE BULLET
    0x0ae1: 0x25ab, #          enopensquarebullet ▫ WHITE SMALL SQUARE
    0x0ae2: 0x25ad, #              openrectbullet ▭ WHITE RECTANGLE
    0x0ae3: 0x25b3, #             opentribulletup △ WHITE UP-POINTING TRIANGLE
    0x0ae4: 0x25bd, #           opentribulletdown ▽ WHITE DOWN-POINTING TRIANGLE
    0x0ae5: 0x2606, #                    openstar ☆ WHITE STAR
    0x0ae6: 0x2022, #          enfilledcircbullet • BULLET
    0x0ae7: 0x25aa, #            enfilledsqbullet ▪ BLACK SMALL SQUARE
    0x0ae8: 0x25b2, #           filledtribulletup ▲ BLACK UP-POINTING TRIANGLE
    0x0ae9: 0x25bc, #         filledtribulletdown ▼ BLACK DOWN-POINTING TRIANGLE
    0x0aea: 0x261c, #                 leftpointer ☜ WHITE LEFT POINTING INDEX
    0x0aeb: 0x261e, #                rightpointer ☞ WHITE RIGHT POINTING INDEX
    0x0aec: 0x2663, #                        club ♣ BLACK CLUB SUIT
    0x0aed: 0x2666, #                     diamond ♦ BLACK DIAMOND SUIT
    0x0aee: 0x2665, #                       heart ♥ BLACK HEART SUIT
    0x0af0: 0x2720, #                maltesecross ✠ MALTESE CROSS
    0x0af1: 0x2020, #                      dagger † DAGGER
    0x0af2: 0x2021, #                doubledagger ‡ DOUBLE DAGGER
    0x0af3: 0x2713, #                   checkmark ✓ CHECK MARK
    0x0af4: 0x2717, #                 ballotcross ✗ BALLOT X
    0x0af5: 0x266f, #                musicalsharp ♯ MUSIC SHARP SIGN
    0x0af6: 0x266d, #                 musicalflat ♭ MUSIC FLAT SIGN
    0x0af7: 0x2642, #                  malesymbol ♂ MALE SIGN
    0x0af8: 0x2640, #                femalesymbol ♀ FEMALE SIGN
    0x0af9: 0x260e, #                   telephone ☎ BLACK TELEPHONE
    0x0afa: 0x2315, #           telephonerecorder ⌕ TELEPHONE RECORDER
    0x0afb: 0x2117, #         phonographcopyright ℗ SOUND RECORDING COPYRIGHT
    0x0afc: 0x2038, #                       caret ‸ CARET
    0x0afd: 0x201a, #          singlelowquotemark ‚ SINGLE LOW-9 QUOTATION MARK
    0x0afe: 0x201e, #          doublelowquotemark „ DOUBLE LOW-9 QUOTATION MARK
    #  0x0aff                                  cursor ? ???
    0x0ba3: 0x003c, #                   leftcaret < LESS-THAN SIGN
    0x0ba6: 0x003e, #                  rightcaret > GREATER-THAN SIGN
    0x0ba8: 0x2228, #                   downcaret ∨ LOGICAL OR
    0x0ba9: 0x2227, #                     upcaret ∧ LOGICAL AND
    0x0bc0: 0x00af, #                     overbar ¯ MACRON
    0x0bc2: 0x22a4, #                    downtack ⊤ DOWN TACK
    0x0bc3: 0x2229, #                      upshoe ∩ INTERSECTION
    0x0bc4: 0x230a, #                   downstile ⌊ LEFT FLOOR
    0x0bc6: 0x005f, #                    underbar _ LOW LINE
    0x0bca: 0x2218, #                         jot ∘ RING OPERATOR
    0x0bcc: 0x2395, #                        quad ⎕ APL FUNCTIONAL SYMBOL QUAD (Unicode 3.0)
    0x0bce: 0x22a5, #                      uptack ⊥ UP TACK
    0x0bcf: 0x25cb, #                      circle ○ WHITE CIRCLE
    0x0bd3: 0x2308, #                     upstile ⌈ LEFT CEILING
    0x0bd6: 0x222a, #                    downshoe ∪ UNION
    0x0bd8: 0x2283, #                   rightshoe ⊃ SUPERSET OF
    0x0bda: 0x2282, #                    leftshoe ⊂ SUBSET OF
    0x0bdc: 0x22a3, #                    lefttack ⊣ LEFT TACK
    0x0bfc: 0x22a2, #                   righttack ⊢ RIGHT TACK
    0x0cdf: 0x2017, #        hebrew_doublelowline ‗ DOUBLE LOW LINE
    0x0ce0: 0x05d0, #                hebrew_aleph א HEBREW LETTER ALEF
    0x0ce1: 0x05d1, #                  hebrew_bet ב HEBREW LETTER BET
    0x0ce2: 0x05d2, #                hebrew_gimel ג HEBREW LETTER GIMEL
    0x0ce3: 0x05d3, #                hebrew_dalet ד HEBREW LETTER DALET
    0x0ce4: 0x05d4, #                   hebrew_he ה HEBREW LETTER HE
    0x0ce5: 0x05d5, #                  hebrew_waw ו HEBREW LETTER VAV
    0x0ce6: 0x05d6, #                 hebrew_zain ז HEBREW LETTER ZAYIN
    0x0ce7: 0x05d7, #                 hebrew_chet ח HEBREW LETTER HET
    0x0ce8: 0x05d8, #                  hebrew_tet ט HEBREW LETTER TET
    0x0ce9: 0x05d9, #                  hebrew_yod י HEBREW LETTER YOD
    0x0cea: 0x05da, #            hebrew_finalkaph ך HEBREW LETTER FINAL KAF
    0x0ceb: 0x05db, #                 hebrew_kaph כ HEBREW LETTER KAF
    0x0cec: 0x05dc, #                hebrew_lamed ל HEBREW LETTER LAMED
    0x0ced: 0x05dd, #             hebrew_finalmem ם HEBREW LETTER FINAL MEM
    0x0cee: 0x05de, #                  hebrew_mem מ HEBREW LETTER MEM
    0x0cef: 0x05df, #             hebrew_finalnun ן HEBREW LETTER FINAL NUN
    0x0cf0: 0x05e0, #                  hebrew_nun נ HEBREW LETTER NUN
    0x0cf1: 0x05e1, #               hebrew_samech ס HEBREW LETTER SAMEKH
    0x0cf2: 0x05e2, #                 hebrew_ayin ע HEBREW LETTER AYIN
    0x0cf3: 0x05e3, #              hebrew_finalpe ף HEBREW LETTER FINAL PE
    0x0cf4: 0x05e4, #                   hebrew_pe פ HEBREW LETTER PE
    0x0cf5: 0x05e5, #            hebrew_finalzade ץ HEBREW LETTER FINAL TSADI
    0x0cf6: 0x05e6, #                 hebrew_zade צ HEBREW LETTER TSADI
    0x0cf7: 0x05e7, #                 hebrew_qoph ק HEBREW LETTER QOF
    0x0cf8: 0x05e8, #                 hebrew_resh ר HEBREW LETTER RESH
    0x0cf9: 0x05e9, #                 hebrew_shin ש HEBREW LETTER SHIN
    0x0cfa: 0x05ea, #                  hebrew_taw ת HEBREW LETTER TAV
    0x0da1: 0x0e01, #                  Thai_kokai ก THAI CHARACTER KO KAI
    0x0da2: 0x0e02, #                Thai_khokhai ข THAI CHARACTER KHO KHAI
    0x0da3: 0x0e03, #               Thai_khokhuat ฃ THAI CHARACTER KHO KHUAT
    0x0da4: 0x0e04, #               Thai_khokhwai ค THAI CHARACTER KHO KHWAI
    0x0da5: 0x0e05, #                Thai_khokhon ฅ THAI CHARACTER KHO KHON
    0x0da6: 0x0e06, #             Thai_khorakhang ฆ THAI CHARACTER KHO RAKHANG
    0x0da7: 0x0e07, #                 Thai_ngongu ง THAI CHARACTER NGO NGU
    0x0da8: 0x0e08, #                Thai_chochan จ THAI CHARACTER CHO CHAN
    0x0da9: 0x0e09, #               Thai_choching ฉ THAI CHARACTER CHO CHING
    0x0daa: 0x0e0a, #               Thai_chochang ช THAI CHARACTER CHO CHANG
    0x0dab: 0x0e0b, #                   Thai_soso ซ THAI CHARACTER SO SO
    0x0dac: 0x0e0c, #                Thai_chochoe ฌ THAI CHARACTER CHO CHOE
    0x0dad: 0x0e0d, #                 Thai_yoying ญ THAI CHARACTER YO YING
    0x0dae: 0x0e0e, #                Thai_dochada ฎ THAI CHARACTER DO CHADA
    0x0daf: 0x0e0f, #                Thai_topatak ฏ THAI CHARACTER TO PATAK
    0x0db0: 0x0e10, #                Thai_thothan ฐ THAI CHARACTER THO THAN
    0x0db1: 0x0e11, #          Thai_thonangmontho ฑ THAI CHARACTER THO NANGMONTHO
    0x0db2: 0x0e12, #             Thai_thophuthao ฒ THAI CHARACTER THO PHUTHAO
    0x0db3: 0x0e13, #                  Thai_nonen ณ THAI CHARACTER NO NEN
    0x0db4: 0x0e14, #                  Thai_dodek ด THAI CHARACTER DO DEK
    0x0db5: 0x0e15, #                  Thai_totao ต THAI CHARACTER TO TAO
    0x0db6: 0x0e16, #               Thai_thothung ถ THAI CHARACTER THO THUNG
    0x0db7: 0x0e17, #              Thai_thothahan ท THAI CHARACTER THO THAHAN
    0x0db8: 0x0e18, #               Thai_thothong ธ THAI CHARACTER THO THONG
    0x0db9: 0x0e19, #                   Thai_nonu น THAI CHARACTER NO NU
    0x0dba: 0x0e1a, #               Thai_bobaimai บ THAI CHARACTER BO BAIMAI
    0x0dbb: 0x0e1b, #                  Thai_popla ป THAI CHARACTER PO PLA
    0x0dbc: 0x0e1c, #               Thai_phophung ผ THAI CHARACTER PHO PHUNG
    0x0dbd: 0x0e1d, #                   Thai_fofa ฝ THAI CHARACTER FO FA
    0x0dbe: 0x0e1e, #                Thai_phophan พ THAI CHARACTER PHO PHAN
    0x0dbf: 0x0e1f, #                  Thai_fofan ฟ THAI CHARACTER FO FAN
    0x0dc0: 0x0e20, #             Thai_phosamphao ภ THAI CHARACTER PHO SAMPHAO
    0x0dc1: 0x0e21, #                   Thai_moma ม THAI CHARACTER MO MA
    0x0dc2: 0x0e22, #                  Thai_yoyak ย THAI CHARACTER YO YAK
    0x0dc3: 0x0e23, #                  Thai_rorua ร THAI CHARACTER RO RUA
    0x0dc4: 0x0e24, #                     Thai_ru ฤ THAI CHARACTER RU
    0x0dc5: 0x0e25, #                 Thai_loling ล THAI CHARACTER LO LING
    0x0dc6: 0x0e26, #                     Thai_lu ฦ THAI CHARACTER LU
    0x0dc7: 0x0e27, #                 Thai_wowaen ว THAI CHARACTER WO WAEN
    0x0dc8: 0x0e28, #                 Thai_sosala ศ THAI CHARACTER SO SALA
    0x0dc9: 0x0e29, #                 Thai_sorusi ษ THAI CHARACTER SO RUSI
    0x0dca: 0x0e2a, #                  Thai_sosua ส THAI CHARACTER SO SUA
    0x0dcb: 0x0e2b, #                  Thai_hohip ห THAI CHARACTER HO HIP
    0x0dcc: 0x0e2c, #                Thai_lochula ฬ THAI CHARACTER LO CHULA
    0x0dcd: 0x0e2d, #                   Thai_oang อ THAI CHARACTER O ANG
    0x0dce: 0x0e2e, #               Thai_honokhuk ฮ THAI CHARACTER HO NOKHUK
    0x0dcf: 0x0e2f, #              Thai_paiyannoi ฯ THAI CHARACTER PAIYANNOI
    0x0dd0: 0x0e30, #                  Thai_saraa ะ THAI CHARACTER SARA A
    0x0dd1: 0x0e31, #             Thai_maihanakat ั THAI CHARACTER MAI HAN-AKAT
    0x0dd2: 0x0e32, #                 Thai_saraaa า THAI CHARACTER SARA AA
    0x0dd3: 0x0e33, #                 Thai_saraam ำ THAI CHARACTER SARA AM
    0x0dd4: 0x0e34, #                  Thai_sarai ิ THAI CHARACTER SARA I
    0x0dd5: 0x0e35, #                 Thai_saraii ี THAI CHARACTER SARA II
    0x0dd6: 0x0e36, #                 Thai_saraue ึ THAI CHARACTER SARA UE
    0x0dd7: 0x0e37, #                Thai_sarauee ื THAI CHARACTER SARA UEE
    0x0dd8: 0x0e38, #                  Thai_sarau ุ THAI CHARACTER SARA U
    0x0dd9: 0x0e39, #                 Thai_sarauu ู THAI CHARACTER SARA UU
    0x0dda: 0x0e3a, #                Thai_phinthu ฺ THAI CHARACTER PHINTHU
    0x0dde: 0x0e3e, #      Thai_maihanakat_maitho ฾ ???
    0x0ddf: 0x0e3f, #                   Thai_baht ฿ THAI CURRENCY SYMBOL BAHT
    0x0de0: 0x0e40, #                  Thai_sarae เ THAI CHARACTER SARA E
    0x0de1: 0x0e41, #                 Thai_saraae แ THAI CHARACTER SARA AE
    0x0de2: 0x0e42, #                  Thai_sarao โ THAI CHARACTER SARA O
    0x0de3: 0x0e43, #          Thai_saraaimaimuan ใ THAI CHARACTER SARA AI MAIMUAN
    0x0de4: 0x0e44, #         Thai_saraaimaimalai ไ THAI CHARACTER SARA AI MAIMALAI
    0x0de5: 0x0e45, #            Thai_lakkhangyao ๅ THAI CHARACTER LAKKHANGYAO
    0x0de6: 0x0e46, #               Thai_maiyamok ๆ THAI CHARACTER MAIYAMOK
    0x0de7: 0x0e47, #              Thai_maitaikhu ็ THAI CHARACTER MAITAIKHU
    0x0de8: 0x0e48, #                  Thai_maiek ่ THAI CHARACTER MAI EK
    0x0de9: 0x0e49, #                 Thai_maitho ้ THAI CHARACTER MAI THO
    0x0dea: 0x0e4a, #                 Thai_maitri ๊ THAI CHARACTER MAI TRI
    0x0deb: 0x0e4b, #            Thai_maichattawa ๋ THAI CHARACTER MAI CHATTAWA
    0x0dec: 0x0e4c, #            Thai_thanthakhat ์ THAI CHARACTER THANTHAKHAT
    0x0ded: 0x0e4d, #               Thai_nikhahit ํ THAI CHARACTER NIKHAHIT
    0x0df0: 0x0e50, #                 Thai_leksun ๐ THAI DIGIT ZERO
    0x0df1: 0x0e51, #                Thai_leknung ๑ THAI DIGIT ONE
    0x0df2: 0x0e52, #                Thai_leksong ๒ THAI DIGIT TWO
    0x0df3: 0x0e53, #                 Thai_leksam ๓ THAI DIGIT THREE
    0x0df4: 0x0e54, #                  Thai_leksi ๔ THAI DIGIT FOUR
    0x0df5: 0x0e55, #                  Thai_lekha ๕ THAI DIGIT FIVE
    0x0df6: 0x0e56, #                 Thai_lekhok ๖ THAI DIGIT SIX
    0x0df7: 0x0e57, #                Thai_lekchet ๗ THAI DIGIT SEVEN
    0x0df8: 0x0e58, #                Thai_lekpaet ๘ THAI DIGIT EIGHT
    0x0df9: 0x0e59, #                 Thai_lekkao ๙ THAI DIGIT NINE
    0x0ea1: 0x3131, #               Hangul_Kiyeog ㄱ HANGUL LETTER KIYEOK
    0x0ea2: 0x3132, #          Hangul_SsangKiyeog ㄲ HANGUL LETTER SSANGKIYEOK
    0x0ea3: 0x3133, #           Hangul_KiyeogSios ㄳ HANGUL LETTER KIYEOK-SIOS
    0x0ea4: 0x3134, #                Hangul_Nieun ㄴ HANGUL LETTER NIEUN
    0x0ea5: 0x3135, #           Hangul_NieunJieuj ㄵ HANGUL LETTER NIEUN-CIEUC
    0x0ea6: 0x3136, #           Hangul_NieunHieuh ㄶ HANGUL LETTER NIEUN-HIEUH
    0x0ea7: 0x3137, #               Hangul_Dikeud ㄷ HANGUL LETTER TIKEUT
    0x0ea8: 0x3138, #          Hangul_SsangDikeud ㄸ HANGUL LETTER SSANGTIKEUT
    0x0ea9: 0x3139, #                Hangul_Rieul ㄹ HANGUL LETTER RIEUL
    0x0eaa: 0x313a, #          Hangul_RieulKiyeog ㄺ HANGUL LETTER RIEUL-KIYEOK
    0x0eab: 0x313b, #           Hangul_RieulMieum ㄻ HANGUL LETTER RIEUL-MIEUM
    0x0eac: 0x313c, #           Hangul_RieulPieub ㄼ HANGUL LETTER RIEUL-PIEUP
    0x0ead: 0x313d, #            Hangul_RieulSios ㄽ HANGUL LETTER RIEUL-SIOS
    0x0eae: 0x313e, #           Hangul_RieulTieut ㄾ HANGUL LETTER RIEUL-THIEUTH
    0x0eaf: 0x313f, #          Hangul_RieulPhieuf ㄿ HANGUL LETTER RIEUL-PHIEUPH
    0x0eb0: 0x3140, #           Hangul_RieulHieuh ㅀ HANGUL LETTER RIEUL-HIEUH
    0x0eb1: 0x3141, #                Hangul_Mieum ㅁ HANGUL LETTER MIEUM
    0x0eb2: 0x3142, #                Hangul_Pieub ㅂ HANGUL LETTER PIEUP
    0x0eb3: 0x3143, #           Hangul_SsangPieub ㅃ HANGUL LETTER SSANGPIEUP
    0x0eb4: 0x3144, #            Hangul_PieubSios ㅄ HANGUL LETTER PIEUP-SIOS
    0x0eb5: 0x3145, #                 Hangul_Sios ㅅ HANGUL LETTER SIOS
    0x0eb6: 0x3146, #            Hangul_SsangSios ㅆ HANGUL LETTER SSANGSIOS
    0x0eb7: 0x3147, #                Hangul_Ieung ㅇ HANGUL LETTER IEUNG
    0x0eb8: 0x3148, #                Hangul_Jieuj ㅈ HANGUL LETTER CIEUC
    0x0eb9: 0x3149, #           Hangul_SsangJieuj ㅉ HANGUL LETTER SSANGCIEUC
    0x0eba: 0x314a, #                Hangul_Cieuc ㅊ HANGUL LETTER CHIEUCH
    0x0ebb: 0x314b, #               Hangul_Khieuq ㅋ HANGUL LETTER KHIEUKH
    0x0ebc: 0x314c, #                Hangul_Tieut ㅌ HANGUL LETTER THIEUTH
    0x0ebd: 0x314d, #               Hangul_Phieuf ㅍ HANGUL LETTER PHIEUPH
    0x0ebe: 0x314e, #                Hangul_Hieuh ㅎ HANGUL LETTER HIEUH
    0x0ebf: 0x314f, #                    Hangul_A ㅏ HANGUL LETTER A
    0x0ec0: 0x3150, #                   Hangul_AE ㅐ HANGUL LETTER AE
    0x0ec1: 0x3151, #                   Hangul_YA ㅑ HANGUL LETTER YA
    0x0ec2: 0x3152, #                  Hangul_YAE ㅒ HANGUL LETTER YAE
    0x0ec3: 0x3153, #                   Hangul_EO ㅓ HANGUL LETTER EO
    0x0ec4: 0x3154, #                    Hangul_E ㅔ HANGUL LETTER E
    0x0ec5: 0x3155, #                  Hangul_YEO ㅕ HANGUL LETTER YEO
    0x0ec6: 0x3156, #                   Hangul_YE ㅖ HANGUL LETTER YE
    0x0ec7: 0x3157, #                    Hangul_O ㅗ HANGUL LETTER O
    0x0ec8: 0x3158, #                   Hangul_WA ㅘ HANGUL LETTER WA
    0x0ec9: 0x3159, #                  Hangul_WAE ㅙ HANGUL LETTER WAE
    0x0eca: 0x315a, #                   Hangul_OE ㅚ HANGUL LETTER OE
    0x0ecb: 0x315b, #                   Hangul_YO ㅛ HANGUL LETTER YO
    0x0ecc: 0x315c, #                    Hangul_U ㅜ HANGUL LETTER U
    0x0ecd: 0x315d, #                  Hangul_WEO ㅝ HANGUL LETTER WEO
    0x0ece: 0x315e, #                   Hangul_WE ㅞ HANGUL LETTER WE
    0x0ecf: 0x315f, #                   Hangul_WI ㅟ HANGUL LETTER WI
    0x0ed0: 0x3160, #                   Hangul_YU ㅠ HANGUL LETTER YU
    0x0ed1: 0x3161, #                   Hangul_EU ㅡ HANGUL LETTER EU
    0x0ed2: 0x3162, #                   Hangul_YI ㅢ HANGUL LETTER YI
    0x0ed3: 0x3163, #                    Hangul_I ㅣ HANGUL LETTER I
    0x0ed4: 0x11a8, #             Hangul_J_Kiyeog ᆨ HANGUL JONGSEONG KIYEOK
    0x0ed5: 0x11a9, #        Hangul_J_SsangKiyeog ᆩ HANGUL JONGSEONG SSANGKIYEOK
    0x0ed6: 0x11aa, #         Hangul_J_KiyeogSios ᆪ HANGUL JONGSEONG KIYEOK-SIOS
    0x0ed7: 0x11ab, #              Hangul_J_Nieun ᆫ HANGUL JONGSEONG NIEUN
    0x0ed8: 0x11ac, #         Hangul_J_NieunJieuj ᆬ HANGUL JONGSEONG NIEUN-CIEUC
    0x0ed9: 0x11ad, #         Hangul_J_NieunHieuh ᆭ HANGUL JONGSEONG NIEUN-HIEUH
    0x0eda: 0x11ae, #             Hangul_J_Dikeud ᆮ HANGUL JONGSEONG TIKEUT
    0x0edb: 0x11af, #              Hangul_J_Rieul ᆯ HANGUL JONGSEONG RIEUL
    0x0edc: 0x11b0, #        Hangul_J_RieulKiyeog ᆰ HANGUL JONGSEONG RIEUL-KIYEOK
    0x0edd: 0x11b1, #         Hangul_J_RieulMieum ᆱ HANGUL JONGSEONG RIEUL-MIEUM
    0x0ede: 0x11b2, #         Hangul_J_RieulPieub ᆲ HANGUL JONGSEONG RIEUL-PIEUP
    0x0edf: 0x11b3, #          Hangul_J_RieulSios ᆳ HANGUL JONGSEONG RIEUL-SIOS
    0x0ee0: 0x11b4, #         Hangul_J_RieulTieut ᆴ HANGUL JONGSEONG RIEUL-THIEUTH
    0x0ee1: 0x11b5, #        Hangul_J_RieulPhieuf ᆵ HANGUL JONGSEONG RIEUL-PHIEUPH
    0x0ee2: 0x11b6, #         Hangul_J_RieulHieuh ᆶ HANGUL JONGSEONG RIEUL-HIEUH
    0x0ee3: 0x11b7, #              Hangul_J_Mieum ᆷ HANGUL JONGSEONG MIEUM
    0x0ee4: 0x11b8, #              Hangul_J_Pieub ᆸ HANGUL JONGSEONG PIEUP
    0x0ee5: 0x11b9, #          Hangul_J_PieubSios ᆹ HANGUL JONGSEONG PIEUP-SIOS
    0x0ee6: 0x11ba, #               Hangul_J_Sios ᆺ HANGUL JONGSEONG SIOS
    0x0ee7: 0x11bb, #          Hangul_J_SsangSios ᆻ HANGUL JONGSEONG SSANGSIOS
    0x0ee8: 0x11bc, #              Hangul_J_Ieung ᆼ HANGUL JONGSEONG IEUNG
    0x0ee9: 0x11bd, #              Hangul_J_Jieuj ᆽ HANGUL JONGSEONG CIEUC
    0x0eea: 0x11be, #              Hangul_J_Cieuc ᆾ HANGUL JONGSEONG CHIEUCH
    0x0eeb: 0x11bf, #             Hangul_J_Khieuq ᆿ HANGUL JONGSEONG KHIEUKH
    0x0eec: 0x11c0, #              Hangul_J_Tieut ᇀ HANGUL JONGSEONG THIEUTH
    0x0eed: 0x11c1, #             Hangul_J_Phieuf ᇁ HANGUL JONGSEONG PHIEUPH
    0x0eee: 0x11c2, #              Hangul_J_Hieuh ᇂ HANGUL JONGSEONG HIEUH
    0x0eef: 0x316d, #     Hangul_RieulYeorinHieuh ㅭ HANGUL LETTER RIEUL-YEORINHIEUH
    0x0ef0: 0x3171, #    Hangul_SunkyeongeumMieum ㅱ HANGUL LETTER KAPYEOUNMIEUM
    0x0ef1: 0x3178, #    Hangul_SunkyeongeumPieub ㅸ HANGUL LETTER KAPYEOUNPIEUP
    0x0ef2: 0x317f, #              Hangul_PanSios ㅿ HANGUL LETTER PANSIOS
    0x0ef3: 0x3181, #    Hangul_KkogjiDalrinIeung ㆁ HANGUL LETTER YESIEUNG
    0x0ef4: 0x3184, #   Hangul_SunkyeongeumPhieuf ㆄ HANGUL LETTER KAPYEOUNPHIEUPH
    0x0ef5: 0x3186, #          Hangul_YeorinHieuh ㆆ HANGUL LETTER YEORINHIEUH
    0x0ef6: 0x318d, #                Hangul_AraeA ㆍ HANGUL LETTER ARAEA
    0x0ef7: 0x318e, #               Hangul_AraeAE ㆎ HANGUL LETTER ARAEAE
    0x0ef8: 0x11eb, #            Hangul_J_PanSios ᇫ HANGUL JONGSEONG PANSIOS
    0x0ef9: 0x11f0, #  Hangul_J_KkogjiDalrinIeung ᇰ HANGUL JONGSEONG YESIEUNG
    0x0efa: 0x11f9, #        Hangul_J_YeorinHieuh ᇹ HANGUL JONGSEONG YEORINHIEUH
    0x0eff: 0x20a9, #                  Korean_Won ₩ WON SIGN
    0x13bc: 0x0152, #                          OE Œ LATIN CAPITAL LIGATURE OE
    0x13bd: 0x0153, #                          oe œ LATIN SMALL LIGATURE OE
    0x13be: 0x0178, #                  Ydiaeresis Ÿ LATIN CAPITAL LETTER Y WITH DIAERESIS
    0x20ac: 0x20ac, #                    EuroSign € EURO SIGN
}
