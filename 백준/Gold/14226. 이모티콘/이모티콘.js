const sol = (S) => {
  const MAX_SIZE = 1000;
  const check = Array.from({ length: MAX_SIZE + 1 }, () => Array(MAX_SIZE + 1).fill(0));
    // check배열은 2차원이면서 (next, clipBoard) 값을 가지므로 최대 (S,S) = (1000,1000) 크기까지 고려해야 한다.

  function bfs() {
    const queue = [];
    queue.push([1, 0, 0]); // 큐에 [현재위치, 클립보드, 시간] 값을 넣어준다.
    check[1][0] = 1; // (현재위치 : 1, 클립보드 : 0)에 방문처리한다.

    while (queue.length) {
      const [now, clipBoard, time] = queue.shift(); // 큐이므로 shift 메서드를 사용하는 것에 유의한다.
      if (now === S) return time;
      if (0 >= now || now > MAX_SIZE) continue; // S의 범위는 2<=S<=1000을 가진다.

      if (!check[now][now]) { // 연산 1. 클립보드에 현재 화면의 이모티콘 수를 저장하기
        check[now][now] = 1;
        queue.push([now, now, time + 1]);
      } 

      if (clipBoard && now + clipBoard <= MAX_SIZE) { // 연산 2. 클립보드에 있는 이모티콘을 화면에 붙여넣기
        if (!check[now + clipBoard][clipBoard]) {
          check[now + clipBoard][clipBoard] = 1;
          queue.push([now + clipBoard, clipBoard, time + 1]);
        }
      }

      if (!check[now - 1][clipBoard]) { // 연산 3. 화면의 이모티콘 중 한 개 삭제하기
        check[now - 1][clipBoard] = 1;
        queue.push([now - 1, clipBoard, time + 1]);
      }
    }
  }

  return bfs();
};

// 백준에서 입력을 받는 코드
require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    console.log(sol(+line));
  })
  .on("close", () => {
    process.exit();
  });