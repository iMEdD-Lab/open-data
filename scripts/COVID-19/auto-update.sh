#!/bin/bash

PROJECT_ROOT=$(dirname $(dirname $(dirname $(realpath $0 ))))
echo "ENTERING PROJECT ROOT" $PROJECT_ROOT

cd $PROJECT_ROOT

mkdir -p "$PROJECT_ROOT/COVID-19/charts"

NOW="$(date)"

echo "PULL FROM MASTER"
git pull origin master

create_commit()
{
    echo "ADD FILES"
    git add *

    echo "COMMIT COMMENTS"
    git commit -a -m "automated commit ($NOW)"

    echo "PUSH COMMENTS"
    git push origin master

    if [[ $? != 0 ]]; then
        echo "PUSH FAILED"
        exit 1
    fi
}

run_updater()
{
    python "scripts/COVID-19/update_data.py" $PROJECT_ROOT
    if [[ $? = 0 ]]; then
        echo "create commit $NOW"
        # create_commit
    else
        echo "failure: $?"
        exit 1
    fi
}

run_updater
