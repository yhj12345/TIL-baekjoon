const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let S = fs.readFileSync(filePath).toString();

const stack = [];
let flag = false;
let ans = 0;

for (let s of S) {
  if (s === "(" || s === "[") {
    stack.push(s);
  } else if (s === ")") {
    let tmp = 0;
    while (true) {
      if (stack.length === 0) {
        flag = true;
        break;
      }

      if (stack[stack.length - 1] === "[") {
        flag = true;
        break;
      } else if (stack[stack.length - 1] === "(") {
        stack.pop();
        if (tmp) {
          stack.push(tmp * 2);
        } else {
          stack.push(2);
        }
        break;
      } else {
        tmp += stack.pop();
      }
    }
  } else if (s === "]") {
    let tmp = 0;
    while (true) {
      if (stack.length === 0) {
        flag = true;
        break;
      }

      if (stack[stack.length - 1] === "(") {
        flag = true;
        break;
      } else if (stack[stack.length - 1] === "[") {
        stack.pop();
        if (tmp) {
          stack.push(tmp * 3);
        } else {
          stack.push(3);
        }
        break;
      } else {
        tmp += stack.pop();
      }
    }
  }

  if (flag) break;
}

for (let s of stack) {
  if (typeof s === "string") {
    flag = true;
    break;
  }
}

if (flag) {
  console.log(0);
} else {
  stack.forEach((num) => {
    ans += num;
  });
  console.log(ans);
}
