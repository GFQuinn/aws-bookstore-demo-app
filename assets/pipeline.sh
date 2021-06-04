set -e
npm i --save-dev enzyme enzyme-adapter-react-16
npm test -- --watchAll=false
npm install
python3 commenttest.py
npm run build
