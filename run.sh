# 1. DELETE the old database
mysql --host=127.0.0.1 --port=3307 -u root -proot -e "DROP DATABASE IF EXISTS biu_shoes;"

# 2. Run all scripts from the beginning
python3 q1.py && \
for i in {1..10}; do python3 q2_$i.py; done && \
for i in {1..10}; do python3 q3_$i.py; done && \
python3 q4.py && \
python3 q5.py && \
for i in {1..5}; do python3 q6_$i.py; done && \
python3 q7.py && \
python3 q8.py && \
python3 q9.py && \
python3 q10.py && \
python3 q11_1.py && \
python3 q11_2.py && \
python3 q12.py
