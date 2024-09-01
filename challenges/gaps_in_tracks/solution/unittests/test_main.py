import json
from unittest.mock import patch, MagicMock
from solution.main import main

@patch('solution.main.get_connection')
@patch('solution.main.calculate_gaps')
@patch('solution.main.process_results')
def test_main(mock_process_results, mock_calculate_gaps, mock_get_connection):
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_get_connection.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    
    mock_calculate_gaps.return_value = [
        ('ABC', 3.000, 4.000),
        ('ABC', 6.000, 7.000),
        ('BCD', 5.000, 6.000)
    ]
    
    mock_process_results.return_value = json.dumps({
        "ABC": [
            {"mileage_from": "3.000", "mileage_to": "4.000"},
            {"mileage_from": "6.000", "mileage_to": "7.000"}
        ],
        "BCD": [
            {"mileage_from": "5.000", "mileage_to": "6.000"}
        ]
    }, indent=4)

    main()

    mock_get_connection.assert_called_once()
    mock_calculate_gaps.assert_called_once_with(mock_cursor)
    mock_process_results.assert_called_once()