echo "Setup server"
python server/server.py &
PROC_ID=$!
sleep 2

echo "Run API tests"
python server/test/test_server.py

echo "Run user simulation tests"
python compass/user_simulator.py

echo "Run compass tests"
python compass/compass.py

echo "Run user tests"
python compass/user.py

echo "Kill server"
kill $PROC_ID
