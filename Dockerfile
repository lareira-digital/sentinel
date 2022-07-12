FROM lareiradigital/base-alpine:py310-hyper-poet as base-image

WORKDIR /app

### COMMON THINGS ###
COPY . /app/
RUN poetry install --no-dev --no-root --no-interaction


#########################################
### FOR NOW ALL OF THIS IS USELESS ######
#########################################

# ### TEST BASE IMAGE ###
# FROM base-image as test-base-image
# ENV WORKERS="1" \
#     LOG_LEVEL="debug"

# RUN poetry install --no-root --no-interaction

# ### BLACK IMAGE ***
# FROM test-base-image as black-test-image

# ENTRYPOINT /entrypoints/black_entrypoint.sh $0 $@

# CMD ["--target-version py310", "--check", " --line-length 80", "."]

# ### UNIT TEST IMAGE ###
# FROM test-base-image as unit-test-image

# ENTRYPOINT /entrypoints/pytest_entrypoint.sh $0 $@

# CMD ["--cov=app", "--cov-report=xml:/test_coverage_reports/unit_tests_coverage.xml"]

### DEVELOPMENT IMAGE ###
FROM base-image as development-image
ENV WORKERS="1" \
    RELOAD="True" \
    LOG_LEVEL="debug"

RUN poetry install --no-root --no-interaction
COPY . /application_root/

# ### PRODUCTION IMAGE ####
# FROM base-image as production-image
# ENV WORKERS="1" \
#     RELOAD="False" \
#     LOG_LEVEL="info"

# RUN poetry install --no-dev --no-root --no-interaction

