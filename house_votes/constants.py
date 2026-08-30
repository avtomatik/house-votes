###############################################################################
# Vote encoding:
###############################################################################
#   1  = yes
#   0  = abstain
#  -1  = no
VOTE_ENCODING = {
    "да": 1,
    "нет": -1,
    "воздержался": 0,
}
###############################################################################
# Party encoding:
###############################################################################
#   0 = Democrat
#   1 = Republican
PARTY_ENCODING = {
    "демократ": 0,
    "республиканец": 1,
}
VOTE_COLUMNS = [
    "Handicapped Infants",
    "Water Project Cost Sharing",
    "Adoption of Budget Resolution",
    "Physician Fee Freeze",
    "El Salvador Aid",
    "Religious Groups in Schools",
    "Anti-Satellite Test Ban",
    "Aid to Nicaraguan Contras",
    "MX Missile",
    "Immigration",
    "Synfuels Corp Cutback",
    "Education Spending",
    "Superfund Right to Sue",
    "Crime",
    "Duty-Free Exports",
    "Export Administration Act / South Africa",
]
TARGET_COLUMN = "Party"
COLUMNS = VOTE_COLUMNS + [TARGET_COLUMN]
