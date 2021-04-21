SHARD_CHOICES = (
    ("Rand", "Rand"),
    ("Mündung", "Mündung"),
    ("Lippe", "Lippe"),
    ("Hals", "Hals"),
    ("Schulter", "Schulter"),
    ("Rumpf", "Rumpf"),
    ("Bauch", "Bauch"),
    ("Boden", "Boden"),
    ("Flachboden", "Flachboden"),
    ("Wackelboden", "Wackelboden"),
    ("Standfuß", "Standfuß"),
    ("Standring", "Standring"),
    ("Knauffuß", "Knauffuß"),
    ("Ganzes Gefäß", "Ganzes Gefäß"),
)

USAGE_CHOCIES = (
    ("Kochgeschirr", "Kochgeschirr"),
    ("Essgeschirr", "Essgeschirr"),
    ("Trinkgeschirr", "Trinkgeschirr"),
    ("Feingeschirr", "Feingeschirr"),
    ("Lagerbehälter", "Lagerbehälter"),
    ("Transportbehälter", "Transportbehälter"),
    ("Vorratsgeschirr", "Vorratsgeschirr"),
    ("Servicegeschirr", "Servicegeschirr"),
    ("Sonstige Verwendung", "Sonstige Verwendung"),
    ("Unbekannt", "Unbekannt"),
)

SURFACE_CHOICES = (
    (None, "---------"),
    ("unbehandelt", "unbehandelt"),
    ("geglättet", "geglättet"),
    ("poliert", "poliert"),
    ("bemalt", "bemalt"),
    ("engobiert", "engobiert"),
    ("glasiert", "glasiert"),
    ("geschnitten", "geschnitten"),
    ("geritzt", "geritzt"),
    ("kammstrichverziert", "kammstrichverziert"),
    ("mit Applikation (frei Hand)", "mit Applikation (frei Hand)"),
    ("mit Applikation (aus der Model)", "mit Applikation (aus der Model)"),
    ("in Barbotine-Technik verziert", "in Barbotine-Technik verziert"),
    ("komplexe Merkmalskombination", "komplexe Merkmalskombination"),
)
CONSERV_CHOICES = (
    ("vollständig", "vollständig"),
    ("annähernd vollständig", "annähernd vollständig"),
    ("sehr gut", "sehr gut"),
    ("gut", "gut"),
    ("mäßig", "mäßig"),
    ("stark fragmentiert", "stark fragmentiert"),
    ("schlecht", "schlecht"),
)

MAN_CHOICES = (
    ("Freigeformt / Handgemacht", "Freigeformt / Handgemacht"),
    ("Langsame Töpferscheibe", "Langsame Töpferscheibe"),
    (
        "Scheibengedreht (Schnelle Töpferscheibe)",
        "Scheibengedreht (Schnelle Töpferscheibe)",
    ),
    ("Modelgeformt", "Modelgeformt"),
    ("Kombinierte Technik", "Kombinierte Technik"),
    ("Sonstiges", "Sonstiges"),
)

BRAND_CHOICES = (
    ("Weich", "Weich"),
    ("Mittel", "Mittel"),
    ("Hart", "Hart"),
    ("Klingend hart", "Klingend hart"),
)
BRAND_ATM_CHOICES = (
    ("Reduzierender Brand", "Reduzierender Brand"),
    ("Oxidierender Brand", "Oxidierender Brand"),
    ("Kombinierte Verfahren", "Kombinierte Verfahren"),
)

ORNAM_CHOICES = (
    ("kammstrichverziert", "kammstrichverziert"),
    ("mit Applikation versehen (frei Hand)", "mit Applikation versehen (frei Hand)"),
    (
        "mt Applikation versehen (aus der Model)",
        "mt Applikation versehen (aus der Model)",
    ),
    ("bemalt", "bemalt"),
    ("glasiert", "glasiert"),
    ("monochrom bemalt", "monochrom bemalt"),
    ("polychrom bemalt", "polychrom bemalt"),
    ("bichrom bemalt", "bichrom bemalt"),
    ("Barbotine-Technik", "Barbotine-Technik"),
    ("unverziert", "unverziert"),
    ("modelgeformt ", "modelgeformt"),
    ("Sonstiges", "Sonstiges"),
    ("Komplexe Merkmalskombination", "Komplexe Merkmalskombination"),
)

MAGER_CHOICES = (
    ("Ungemagert", "Ungemagert"),
    ("Vegetabil", "Vegetabil"),
    ("Vegetabil mit mineralischem Beischlag", "Vegetabil mit mineralischem Beischlag"),
    (
        "Vegetabil mit Schamott und mineralischem Beischlag",
        "Vegetabil mit Schamott und mineralischem Beischlag",
    ),
    ("Mineralisch", "Mineralisch"),
    ("Mineralisch mit vegetabilem Beischlag", "Mineralisch mit vegetabilem Beischlag"),
    (
        "Mineralisch mit Schamott und vegetabilem Beischlag",
        "Mineralisch mit Schamott und vegetabilem Beischlag",
    ),
    ("Schamott", "Schamott"),
    ("Schamott mit vegetabilem Beischlag", "Schamott mit vegetabilem Beischlag"),
    ("Schamott mit mineralischem Beischlag", "Schamott mit mineralischem Beischlag"),
    (
        "Schamott mit vegetabilem und mineralischem Beischlag",
        "Schamott mit vegetabilem und mineralischem Beischlag",
    ),
    ("Komplexe Merkmalskombination", "Komplexe Merkmalskombination"),
    ("Weiteres ", "Weiteres"),
)
MAGER_MENGE_CHOICES = (
    ("0%", "0%"),
    ("1-5%", "1-5%"),
    ("6-10%", "6-10%"),
    ("11-15%", "11-15%"),
    ("16-20%", "16-20%"),
    ("21-25%", "21-25%"),
    ("26-30%", "26-30%"),
    ("31-35%", "31-35%"),
    ("36-40%", "36-40%"),
    ("41-45%", "41-45%"),
    ("46-50%", "46-50%"),
    ("51-55%", "51-55%"),
    ("56-60%", "56-60%"),
    ("61-65%", "61-65%"),
    ("66-70%", "66-70%"),
    ("71-75%", "71-75%"),
    ("76-80%", "76-80%"),
    ("81-85%", "81-85%"),
    ("86-90%", "86-90%"),
    ("91-95%", "91-95%"),
    ("96-100%", "96-100%"),
)

MAGER_SIZE_CHOICES = (
    ("Sehr klein", "Sehr klein"),
    ("Klein", "Klein"),
    ("Mittel", "Mittel"),
    ("Groß", "Groß"),
    ("Sehr Groß", "Sehr Groß"),
)

MAGER_DIST_CHOICES = (
    ("Zufällig verteilt", "Zufällig verteilt"),
    ("Gleichmäßig verteilt", "Gleichmäßig verteilt"),
)

MAGER_FORM_CHOICES = (
    ("Rundlich", "Rundlich"),
    ("Länglich", "Länglich"),
    ("Muschelig", "Muschelig"),
    ("Winkelig", "Winkelig"),
)
