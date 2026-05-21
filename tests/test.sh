#!/bin/bash
set -e

echo "Starting global energy policy analysis verifier..." > /logs/verifier/test-output.log
echo "Verification timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" >> /logs/verifier/test-output.log

# Install any missing dependencies
echo "Checking dependencies..." >> /logs/verifier/test-output.log
pip install -q jsonschema pandas 2>&1 | tee -a /logs/verifier/test-output.log

# Run the verification script
echo "Starting verification script..." >> /logs/verifier/test-output.log
python3 /tests/verify.py 2>&1 | tee -a /logs/verifier/test-output.log
VERIFIER_EXIT_CODE=$?

set -e

# Handle reward file creation
if [ ! -f /logs/verifier/reward.txt ]; then
    echo "Warning: Verifier did not create reward.txt, creating from exit code" >> /logs/verifier/test-output.log
    if [ "${VERIFIER_EXIT_CODE}" -eq 0 ]; then
        echo "1.0" > /logs/verifier/reward.txt
    else
        echo "0.0" > /logs/verifier/reward.txt
    fi
fi

# Log final results
REWARD=$(cat /logs/verifier/reward.txt)
echo "Final verification reward: ${REWARD}" >> /logs/verifier/test-output.log
echo "Verification completed at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" >> /logs/verifier/test-output.log
echo "Exit code: ${VERIFIER_EXIT_CODE}" >> /logs/verifier/test-output.log

exit "${VERIFIER_EXIT_CODE}"
