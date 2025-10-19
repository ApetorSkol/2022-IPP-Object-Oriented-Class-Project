Implementační dokumentace k 1. úloze do IPP 2021/2022
Jméno a příjmení: Matej Slivka
Login: xslivk03

**** Program je interpret IPPcode2021/2022 do jazyka XML.
Program postupne preklada kazdy riadok kódu.
Program zacne odstranenim komentaru a rozdelenim zvysnej lexémy na operand a parameter.
Program vykonáva kontrolu počas interpretácie. Ak nájde chybu tak vracia návratový kód 23/ 22/ 21 podľa chyby
    : 23 predstavuje chybu v syntaxe alebo lexéme
    : 22 predstavuje vnútornú syntaktickú chyba (take nemám ;D  )
    : 21 predstavuje chybu v záhlavý
    : 0 vracia program po úspešnom ukončení
**** Projekt bol implementovaný v jazyku php

Projekt dokáže preložiť príkazy
    MOVE
    CREATEFRRAME
    PUSHFRAME
    POPFRAME
    DEFVAR
    CALL
    RETURN
    PUSHS
    POPS
    ADD
    SUB
    MUL
    IDIV
    LT
    GT
    EQ
    AND
    OR
    NOT
    INT2CHAR
    STRI2INT
    READ
    WRITE
    CONCAT
    STRLEN
    GETHAR
    SETCHAR
    TYPE
    LABEL
    JUMP
    JUMPIFEQ
    JUMPIFNEQ
    EXIT
    DPRINT
    BREAK

**** Prerekvizity:
        Linuxový OS
        parse.php
        stiahnué php
**** Použitie cez príkazový riadok
        php8.1 parse.php << [input]  >> [output]
            kde input je súbor so vstupom
            kde output je súbor do ktorého ma byť vpisaný výstup
    
    Príklad:
         vstup:
         # Ukazka kĂłdu se sĂ©mantickou chybou (skript parse.php ale vracĂ­ 0 mĂ­sto 54), kterĂˇ nemĂˇ bĂ˝t detekovĂˇna uĹľ v parse.php. Obsahuje pĹ™Ă­klad elementu bez podelementĹŻ, kterĂ˝ lze zapsat krĂˇtkĂ˝m i dlouhĂ˝m zpĹŻsobem.
        .IPPcode22
        
        CREATEFRAME # pĹ™Ă­klad instrukce bez operandĹŻ, v XML moĹľnĂ˝ zĂˇpis delĹˇĂ­m zpĹŻsobem
        DEFVAR TF@x
        PUSHFRAME
        CREATEFRAME
        WRITE TF@x  # pĹ™Ă­stup k nedefinovanĂ© promÄ›nnĂ©, coĹľ se v parse.php neodhalĂ­
        POPFRAME # tato instrukce bude pro ilustraci ve vĂ˝stupnĂ­m XML zapsĂˇna kratĹˇĂ­m zpĹŻsobem

        Výstup:
        <?xml version="1.0" encoding="UTF-8"?>
            <program language="IPPcode22">
            <instruction order="1" opcode="CREATEFRAME">
            </instruction>
            <instruction order="2" opcode="DEFVAR">
                <arg1 type="var">TF@x</arg1>
            </instruction>
            <instruction order="3" opcode="PUSHFRAME">
            </instruction>
            <instruction order="4" opcode="CREATEFRAME">
            </instruction>
            <instruction order="5" opcode="WRITE">
                <arg1 type="var">TF@x</arg1>
            </instruction>
            <instruction order="6" opcode="POPFRAME" />
        </program>
