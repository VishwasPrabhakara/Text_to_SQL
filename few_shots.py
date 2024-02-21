few_shots =[
    {
        "Question": "How many t-shirts do we have left for nike in extra small size and white colour",
        'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
        'SQLResult': "Result of the SQL Query",
        "Answer": "77"
    },
    {
        "Question": "How much is the price of the inventory for all small size t-shorts",
        'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size='S'",
        'SQLResult': 'Result of the SQL Query',
        "Answer": "18208"
    },
    {
        "Question": "IF we heave to sell all the LEvi's T-shirts today with discounts applied . how much revenue our store will generate(post discounts)?",
        'SQLQuery': "select sum(a.total_amount * ((100 - COALESCE(discounts.pct_discount, 0)) / 100)) as total_revenue from (select sum(price * stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi' group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id",
        'SQLResult' : "Result of the SQL  Query",
        "Answer": "22075"
    },
    {
        'Question':"if we have to sell all the Levi's T-shirt today.How much revenue our store will generate",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand='Levi'",
        'SQLResult': "Result of the SQL Query",
        "Answer": "22075"
    },
    {
        "Question": "How many white colour Levi's white t shirts we have available",
        'SQLQuery': "SELECt sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
        'SQLResult': "Result of the SQL Query",
        "Answer": "118"
    }
]