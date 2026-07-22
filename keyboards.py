from telegram import ReplyKeyboardMarkup

# =====================================================
# ROLE KEYBOARD
# =====================================================

ROLE_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["Warehouse Engineer"],
        ["Technician"],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    is_persistent=True,
)

# =====================================================
# PLACEMENT LIST
# =====================================================

PLACEMENTS = [
    "ACEH",
    "SO LANGSA",
    "SO LHOKSEUMAWE",
    "SO MEULABOH",
    "SO TAPAKTUAN",
    "SO TAKENGON",
    "SO SIGLI",
    "MEDAN",
    "SO BINJAI",
    "SO PADANG BULAN",
    "SO PUBA",
    "SO SPM",
    "SO SKI",
    "SO TJR",
    "SO TJM",
    "SO LBP",
    "SUMUT",
    "SO KABANJAHE",
    "SO KISARAN",
    "SO SIDEMPUAN",
    "SO PMTG SIANTAR",
    "SO RANTAU PRAPAT",
    "SO SIBOLGA",
]

# =====================================================
# BUILD PLACEMENT KEYBOARD (2 BUTTONS PER ROW)
# =====================================================

placement_buttons = []

for i in range(0, len(PLACEMENTS), 2):
    placement_buttons.append(PLACEMENTS[i:i + 2])

placement_buttons.append(["❌ Cancel"])

PLACEMENT_KEYBOARD = ReplyKeyboardMarkup(
    placement_buttons,
    resize_keyboard=True,
    one_time_keyboard=False,
    is_persistent=True,
)

# =====================================================
# FINISH KEYBOARD
# =====================================================

FINISH_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["🔄 New Report"],
        ["❌ Exit"],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    is_persistent=True,
)
