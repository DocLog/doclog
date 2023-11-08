from datetime import date, datetime

test_parameters = {
    "empty_texts": [
        "",
        " ",
        "   ",
        """
    
        """,
    ],
    "invalid_cpfs": ["00000000000", "11111111111", "invalid_cpf", "123.456.789-10"],
    "invalid_crms": [
        "CRM-123456-SP",
        "CRM/SP 12345",
        "CRN/SP 123456",
        "CRM/XX 123456",
        "CRM/SP 11223344",
        "invalid_crm",
    ],
    "future_dates": [
        datetime(year=9999, month=12, day=31),
        date(year=9999, month=12, day=31),
    ],
    "non_positive_values": [-1, 0, -1e-12],
    "invalid_blood_types": ["ABO", "AB", "", "  "],
    "invalid_emails": [
        "invalid_email",
        "@invalid.com",
        "invalid.com",
        "invalid@invalid",
        "invalid@invalid.",
        "@@invalid.com",
    ],
    "filled_texts": ["Nome", "Rinite", "."],
    "valid_cpfs": [
        "72501750845",
        "49168860625",
        "52732606553",
        "19682307180",
        "71703666658",
        "66817552320",
        "49961015207",
        "96647585907",
    ],
    "valid_crms": ["CRM/SP 123456", "CRM/MG 115312", "CRM/RJ 987654", "CRM/BA 123456"],
    "past_dates": [
        datetime(year=1900, month=1, day=1),
        date(year=1900, month=1, day=1),
    ],
    "positive_values": [1, 1e-12],
    "valid_blood_types": ["AB+", "AB-", "A+", "A-", "B+", "B-", "O+", "O-"],
    "valid_emails": [
        "valid_email@valid_domain.com",
        "valid@email.net",
        "valid123@another_mail_company.org",
    ],
    "passwords": [
        "abc",
        "123",
        "abc123",
        "adm",
        "123456",
        "sa",
        "user",
        "pwd",
        "my_password",
        "A very, very large password that definitely has more than 72 bytes and characters.",
    ],
}


def get_test_parameters(params_key: str):
    return test_parameters[params_key]
