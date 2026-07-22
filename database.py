import gspread
from google.oauth2.service_account import Credentials

from config import SPREADSHEET_ID
from config import GOOGLE_CREDENTIALS

# ==================================================
# GOOGLE AUTHENTICATION
# ==================================================

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(
    GOOGLE_CREDENTIALS,
    scopes=SCOPES,
)

client = gspread.authorize(creds)

worksheet = client.open_by_key(SPREADSHEET_ID).sheet1

# ==================================================
# DATABASE FUNCTIONS
# ==================================================

def get_all_data():
    return worksheet.get_all_records()


def find_rfc(rfc):
    values = worksheet.col_values(1)

    for i, value in enumerate(values, start=1):
        if value == rfc:
            return i

    return None


def rfc_exists(rfc):
    return find_rfc(rfc) is not None


# ==================================================
# CREATE NEW RFC
# ==================================================

def add_rfc(rfc, bg_name, bg_placement):

    worksheet.append_row([
        rfc,            # A
        bg_name,        # B
        bg_placement,   # C
        "",             # D Nama Gudang
        "",             # E Placement Gudang

        "",  # Drop Core
        "",  # Precon50
        "",  # Precon60
        "",  # Precon70
        "",  # Precon75
        "",  # Precon80
        "",  # Precon85
        "",  # Precon100
        "",  # Precon120
        "",  # Precon125
        "",  # Precon130
        "",  # Precon135
        "",  # Precon150
        "",  # Precon200
        "",  # Precon250
        "",  # Clamp-hook
        "",  # S-Clamp S
        "",  # SOC-ILS
        "",  # SOC-FUJ
        "",  # SOC-SUM
        "",  # SN ONT
        "",  # SN STB
    ])


# ==================================================
# SAVE TECHNICIAN INFO
# ==================================================

def save_technician(row, technician_name, technician_placement):

    worksheet.update_cell(row, 4, technician_name)
    worksheet.update_cell(row, 5, technician_placement)


# ==================================================
# SAVE MATERIAL ANSWERS
# ==================================================

def save_materials(row, answers):

    start_column = 6

    for i, value in enumerate(answers):
        worksheet.update_cell(
            row,
            start_column + i,
            value,
        )


# ==================================================
# UPDATE CELL
# ==================================================

def update_cell(row, col, value):
    worksheet.update_cell(row, col, value)


def get_row(row):
    return worksheet.row_values(row)


def print_sheet():
    for row in worksheet.get_all_values():
        print(row)


# ==================================================
# TEST CONNECTION
# ==================================================

if __name__ == "__main__":

    print("Connected Successfully!")
    print("Worksheet :", worksheet.title)
    print("Rows :", worksheet.row_count)
    print("Columns :", worksheet.col_count)
