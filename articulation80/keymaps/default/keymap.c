#include QMK_KEYBOARD_H
#include "keymap_uk.h"

enum Layers {
    LAYER_BASE,
    LAYER_LOWER,
    LAYER_RAISE,
    LAYER_GAME
};

#define KC_AF1 LALT(KC_1)
#define KC_AF2 LALT(KC_2)
#define KC_AF3 LALT(KC_3)
#define KC_AF4 LALT(KC_4)
#define KC_MOLO MO(LAYER_LOWER)
#define KC_MORA MO(LAYER_RAISE)
#define KC_TGRA TG(LAYER_RAISE)
#define KC_TGGA TG(LAYER_GAME)

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [LAYER_BASE] = LAYOUT_split_5x9_4(
        KC_NO   , KC_NO   , KC_NO   , KC_ESC  , KC_F4   , KC_NO   , KC_NO   , KC_NO   , KC_NO             ,           KC_AF4  , KC_AF3  , KC_AF2  , KC_AF1  , KC_PSCR , KC_BSPC , KC_INS  , KC_HOME , KC_PGUP ,
        KC_NO   , KC_NO   , KC_NO   , KC_TAB  , KC_Q    , KC_W    , KC_F    , KC_P    , KC_B              ,           KC_J    , KC_L    , KC_U    , KC_Y    , KC_SCLN , KC_ENT  , KC_DEL  , KC_END  , KC_PGDN ,
        KC_NO   , KC_NO   , KC_NO   , KC_LSFT , KC_A    , KC_R    , KC_S    , KC_T    , KC_G              ,           KC_M    , KC_N    , KC_E    , KC_I    , KC_O    , KC_RSFT , KC_RSFT , KC_UP   , KC_RSFT ,
        KC_NO   , KC_NO   , KC_NO   , KC_LCTL , KC_Z    , KC_X    , KC_C    , KC_D    , KC_V    , KC_TGGA , KC_TGRA , KC_K    , KC_H    , KC_COMM , KC_DOT  , KC_SLSH , KC_RCTL , KC_LEFT , KC_DOWN , KC_RGHT ,
                                                                              KC_LALT , KC_MOLO , KC_BSPC , KC_SPC  , KC_MORA , KC_RGUI
    ),
    [LAYER_LOWER] = LAYOUT_split_5x9_4(
        _______ , _______ , _______ , KC_VOLD , KC_VOLU , _______ , _______ , _______ , _______           ,           KC_NO   , KC_NO   , KC_NO   , KC_NO   , KC_NO   , _______ , KC_F10   , KC_F11 , KC_F12  ,
        _______ , _______ , _______ , _______ , KC_GRV  , UK_HASH , KC_QUOT , KC_SCLN , KC_NO             ,           KC_NO   , KC_AMPR , KC_ASTR , KC_LPRN , KC_RPRN , _______ , KC_F7    , KC_F8  , KC_F9   ,
        _______ , _______ , _______ , _______ , KC_PLUS , KC_LCBR , KC_RCBR , KC_MINS , KC_NO             ,           KC_NO   , KC_DLR  , KC_PERC , KC_CIRC , KC_NO   , _______ , KC_F4    , KC_F5  , KC_F6   ,
        _______ , _______ , _______ , _______ , UK_BSLS , KC_LPRN , KC_RPRN , KC_NO   , KC_NO   , KC_NO   , _______ , KC_NO   , KC_EXLM , UK_DQUO , UK_PND  , KC_NO   , _______ , KC_F1    , KC_F2  , KC_F3   ,
                                                                              _______ , _______ , _______ , _______ , _______ , _______
    ),
    [LAYER_RAISE] = LAYOUT_split_5x9_4(
        _______ , _______ , _______ , KC_VOLD , KC_VOLU , _______ , _______ , _______ , _______           ,           KC_NO   , KC_NUM  , KC_PSLS , KC_PAST , KC_PMNS , _______ , _______ , _______ , _______ ,
        _______ , _______ , _______ , _______ , UK_NOT  , UK_TILD , UK_AT   , KC_COLN , KC_NO             ,           KC_NO   , KC_P7   , KC_P8   , KC_P9   , KC_PPLS , KC_PENT , _______ , _______ , _______ ,
        _______ , _______ , _______ , _______ , KC_EQL  , KC_LBRC , KC_RBRC , KC_UNDS , KC_NO             ,           KC_NO   , KC_P4   , KC_P5   , KC_P6   , KC_PPLS , _______ , _______ , _______ , _______ ,
        _______ , _______ , _______ , _______ , UK_PIPE , KC_NO   , KC_NO   , KC_NO   , KC_NO   , KC_NO   , _______ , KC_NO   , KC_P1   , KC_P2   , KC_P3   , KC_PDOT , _______ , _______ , _______ , _______ ,
                                                                              _______ , _______ , _______ , _______ , _______ , KC_P0
    ),
    [LAYER_GAME] = LAYOUT_split_5x9_4(
        _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______           ,           KC_4    , KC_3    , KC_2    , KC_1    , KC_ESC  , KC_P4   , _______ , _______ , _______ ,
        _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______           ,           KC_R    , KC_E    , KC_W    , KC_Q    , KC_TAB  , KC_P3   , _______ , _______ , _______ ,
        _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______           ,           KC_F    , KC_A    , KC_S    , KC_D    , KC_LSFT , KC_P2   , _______ , _______ , _______ ,
        _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______ , KC_NO   , KC_V    , KC_C    , KC_X    , KC_Z    , KC_LCTL , KC_P1   , _______ , _______ , _______ ,
                                                                              _______ , _______ , _______ , _______ , _______ , _______
    ),
};
