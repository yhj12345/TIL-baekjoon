const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const callNumbers = input.slice(1).map((str) => str.split(" "));
let promisingNums = [];

for (let i = 1; i <= 9; i++) {
  for (let j = 1; j <= 9; j++) {
    for (let k = 1; k <= 9; k++) {
      if (i !== j && j !== k && i !== k) {
        let newNumber = 100 * i + 10 * j + k;
        promisingNums.push(String(newNumber));
      }
    }
  }
}

for (let callNumber of callNumbers) {
  let [number, strike, ball] = callNumber;
  [strike, ball] = [strike, ball].map(Number);
  let nowPromisingNums = [];

  for (let promisingNum of promisingNums) {
    let nowStrike = 0;
    let nowBall = 0;
    for (let i = 0; i <= 2; i++) {
      if (number[i] === promisingNum[i]) {
        nowStrike += 1;
      }
    }

    for (let i = 0; i <= 2; i++) {
      for (let j = 0; j <= 2; j++) {
        if (i !== j && number[i] === promisingNum[j]) {
          nowBall += 1;
        }
      }
    }

    if (nowStrike === strike && nowBall === ball) {
      nowPromisingNums.push(promisingNum);
    }
  }

  promisingNums = nowPromisingNums;
}

console.log(promisingNums.length);
