

class IngredientUnit():
    GRAMM = "g"
    HEKTO = "hg"
    KILO = "kg"
    MILLI_LITER = "ml"
    CENTI_LITER = "cl"
    DECI_LITER = "dl"
    LITER = "l"
    PIECE = "st"
    TEA_SPOON = "tsk"
    TABLE_SPOON = "msk"
    SPICE_SPOON = "krm"

    units = [
        (GRAMM, 'g'),
        (KILO, 'kg'),
        (HEKTO, 'hg'),
        (MILLI_LITER, 'ml'),
        (CENTI_LITER, 'cl'),
        (DECI_LITER, 'dl'),
        (LITER, 'l'),
        (PIECE, 'st'),
        (TEA_SPOON, 'tsk'),
        (TABLE_SPOON, 'msk'),
        (SPICE_SPOON, 'krm'),
    ]


class IngredientCategory():
    VEGETABLE = "VEGETABLE"
    FRUIT = "FRUIT"
    REFRIGERATED = "REFRIGERATED"
    SPICE = "SPICE"
    DRY_GOOD = "DRY_GOOD"

    categories = [
        (VEGETABLE, "Vegetable"),
        (FRUIT, "Fruit"),
        (REFRIGERATED, "Refrigerated"),
        (SPICE, "Spice"),
        (DRY_GOOD, "Dry good"),
    ]

class IngredientReplacementReason:
    VEGITARIAN = "VEGITARIAN"
    VEGAN = "VEGAN"
    DAIRY = "DAIRY"
    GLUTEN = "GLUTEN"
    MP_ALLERGIES = "MP_ALLERGIES"
    LEGUMINOUS = "LEGUMINOUS"

    reasons = [
        (VEGITARIAN, "Vegitarian"),
        (VEGAN, "Vegan"),
        (DAIRY, "Dairy"),
        (GLUTEN, "Gluten"),
        (LEGUMINOUS,"Leguminous"), 
        (MP_ALLERGIES,"MIlk protien")
    ]

