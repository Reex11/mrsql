
from sqlninja import engine as sqlninja


title = "Cohort Analysis"
desc = "Generates an SQL query that does a Cohort Analysis for a chosen target and retention period."

def query(answers):
    return sqlninja.render("templates/cohort.sql",
                            table_name=answers['table_name'],
                            count_column=answers['count_column'],
                            date_column=answers['date_column'],
                            date_unit=answers['date_unit'],
                            aquisition_life=answers['aquisition_life'],
                            aquisition_condition=answers['aquisition_condition'],
                            has_percentage=answers['has_percentage']
                            )

questions = [
    {
        'type': 'input',
        'name': 'table_name',
        'message': "What's the table name?",
        "default": "orders"
    },
    {
        'type': 'input',
        'name': 'count_column',
        'message': "What's the [Target] column name? (Usually, The User ID column)",
        "default": "ibuyerid"
    },
    {
        'type': 'input',
        'name': 'date_column',
        'message': "What's the [Date] column name?",
        "default": "created_at"
    },
    {
        'type': 'list',
        'name': 'date_unit',
        'message': "What's the date unit you want to use?",
        "default": 2,
        'choices': [
            'Year',
            'Month',
            'Week',
            'Day',
            'Hour'
        ],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'number',
        'name': 'aquisition_life',
        'message': lambda result: "How many retention per row? (Number of "+result["date_unit"]+"s)",
        "default": 12,
        "min_allowed": 1,
        'filter': lambda val: int(val)
    },
    {
        'type': 'confirm',
        "name":"has_percentage",
        "message": "Do you want to show results as percentages? (If not, results will be numeric)",
        'default': True
    },
    {
        'type': 'confirm',
        "name":"has_condition",
        "message": "Do you want to specify a condition? (WHERE CLAUSE)",
        'default': False
    },
    {
        'type': 'input',
        "name":"aquisition_condition",
        "message": "Enter the condition - WHERE:",
        "default": "vstatus = 'delivered'",
        'filter': lambda val: "WHERE "+val,
        "when": lambda result: result["has_condition"]
    }

]

