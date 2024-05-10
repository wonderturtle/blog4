# here we delcare all the global variable that we need across the project
# to use: import tw_globals
# to reference them: tw_globals.RET_ALREADY_EXISTING

# for a row that in the db already exists
RET_ALREADY_EXISTING = 1

# for a new row inserted into the db
RET_CREATED = 2

# for an error created by the db
RET_DB_ERROR = 3

# for an error not created by the user
RET_NOT_USER_ERROR = 5

#for a new update
RET_UPDATED = 4

# for row deleted
RET_DELETED = 9


# section for roles
ROLE_ADMIN = 1
ROLE_CUSTOMER = 2
ROLE_VECTOR = 3