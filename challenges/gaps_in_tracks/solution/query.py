# build and execute the self join to identify the gaps
def calculate_gaps(cursor):
    query = """
        SELECT 
            t1.elr_code, 
            t1.mileage_to AS gap_start, 
            t2.mileage_from AS gap_end
        FROM 
            mileages t1
        JOIN 
            mileages t2 
        ON 
            t1.elr_code = t2.elr_code 
            AND t1.mileage_to < t2.mileage_from
        WHERE 
            NOT EXISTS (
                SELECT 1 
                FROM mileages t3 
                WHERE 
                    t3.elr_code = t1.elr_code 
                    AND t3.mileage_from < t2.mileage_from 
                    AND t3.mileage_to > t1.mileage_to
            )
        ORDER BY 
            t1.elr_code, 
            t1.mileage_to;
    """
    cursor.execute(query)
    return cursor.fetchall()