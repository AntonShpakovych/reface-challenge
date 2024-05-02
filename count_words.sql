create function count_words(input_data text) returns integer
    language plpgsql
as
$$
DECLARE
    match_count INTEGER;
BEGIN
    SELECT COUNT(match) INTO match_count
    FROM regexp_matches(input_data, '[a-zA-Z]+', 'g') AS matches(match);

    RETURN match_count;
END;
$$;

alter function count_words(text) owner to postgres;
