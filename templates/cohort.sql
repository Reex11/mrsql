SELECT aquired_period,

{% if has_percentage %}
        CAST( COUNT( distinct CASE WHEN DATE_TRUNC('{{ date_unit }}',{{ table_name }}.{{ date_column }}) = aquired_period THEN {{ table_name }}.{{ count_column }} END ) as float ) as p0

        {% for period_position in range(1,aquisition_life+1) %},
        CAST( COUNT( distinct CASE WHEN DATE_TRUNC('{{ date_unit }}',{{ table_name }}.{{ date_column }}) = DATEADD('{{ date_unit }}',{{ period_position }},aquired_period) THEN {{ table_name }}.{{ count_column }} END ) as float )/p0 as p{{ period_position }}
        {% endfor %}
{% else %}
        COUNT( distinct CASE WHEN DATE_TRUNC('{{ date_unit }}',{{ table_name }}.{{ date_column }}) = aquired_period THEN {{ table_name }}.{{ count_column }} END ) as p0

        {% for period_position in range(1,aquisition_life+1) %},
        COUNT( distinct CASE WHEN DATE_TRUNC('{{ date_unit }}',{{ table_name }}.{{ date_column }}) = DATEADD('{{ date_unit }}',{{ period_position }},aquired_period) THEN {{ table_name }}.{{ count_column }} END ) as p{{ period_position }}
        {% endfor %}
{% endif %}

FROM {{ table_name }}
INNER JOIN (
    SELECT {{ count_column }}, min(DATE_TRUNC('{{ date_unit }}',{{ date_column }})) as aquired_period
    FROM {{ table_name }}
    {{ aquisition_condition or '' }}
    GROUP BY {{ count_column }}
) sub_{{ table_name }} ON {{ table_name }}.{{ count_column }} = sub_{{ table_name }}.{{ count_column }}
{! aquisition_condition or '' !}
GROUP BY aquired_period
ORDER BY aquired_period