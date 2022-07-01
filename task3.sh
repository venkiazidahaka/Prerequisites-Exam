#!/bin/bash
cd /home/user/catkin_ws/src/linux_exam/this/is/my/linux/exam
rm /home/user/catkin_ws/src/linux_exam/this/is/my/linux/exam/*
touch exam1.py
chmod a+r exam1.py
chmod o-x exam1.py
chmod u+x exam1.py
chmod g+x exam1.py
chmod u+w exam1.py
touch exam2.py
chmod a+x exam2.py
chmod o-r exam2.py
chmod u+r exam2.py
chmod u-w exam2.py
chmod g-x exam2.py
chmod g-r exam2.py
chmod g-w exam2.py
touch exam3.py
chmod o+x exam3.py
chmod o-r exam3.py
chmod u+w exam3.py
chmod u-r exam3.py
chmod g+r exam3.py
