create function count_unique_words(input_data text) returns integer
    language plpgsql
as
$$
DECLARE
    match_count INTEGER;
BEGIN
    SELECT COUNT(DISTINCT match) INTO match_count
    FROM regexp_matches(input_data, '[a-zA-Z]+', 'g') AS matches(match);

    RETURN match_count;
END;
$$;

ALTER FUNCTION count_unique_words(text) OWNER TO :owner;
