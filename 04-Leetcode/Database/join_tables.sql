-- Join Tables 378ms runtime
SELECT firstName as FirstName, lastName as LastName, city as City, state as State
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;