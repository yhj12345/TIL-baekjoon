const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const N = input[0]; // 사진틀
const M = input[1]; // 추천횟수
const arr = input[2].split(" ").map(Number); // 추천받은 순서

const recommend = {};
const photoZone = [];

for (let num of arr) {
  let index = photoZone.findIndex((photo) => photo == num);

  if (index === -1) {
    if (photoZone.length < N) {
      photoZone.push(num);
      recommend[num] = 1;
    } else {
      let removeIndex = 0;
      let recommendCount = recommend[photoZone[0]];
      photoZone.forEach((photo, i) => {
        if (recommend[photo] < recommendCount) {
          removeIndex = i;
          recommendCount = recommend[photo];
        }
      });
      let removeItem = photoZone.splice(removeIndex, 1);
      photoZone.push(num);
      recommend[num] = 1;
      recommend[removeItem] = 0;
    }
  } else {
    recommend[num] += 1;
  }
}
photoZone.sort(function (a, b) {
  return a - b;
});
let ans = photoZone.join(" ");
console.log(ans);
