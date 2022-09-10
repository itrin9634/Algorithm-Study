-- 코드를 입력하세요
SELECT @hour := -1;

SELECT(@hour := @hour + 1) AS HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
