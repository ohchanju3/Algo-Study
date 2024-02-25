function solution(a, b, c, d) {
  // 각 숫자의 빈도를 계산
  const counts = {};
  [a, b, c, d].forEach((num) => {
    counts[num] = (counts[num] || 0) + 1;
  });

  // 숫자들의 빈도에 따라 점수를 계산
  const keys = Object.keys(counts);
  if (keys.length === 1) {
    // 네 주사위 숫자가 모두 같은 경우
    return 1111 * parseInt(keys[0]);
  } else if (keys.length === 2) {
    if (counts[keys[0]] === 3 || counts[keys[1]] === 3) {
      // 세 주사위 숫자가 같고 나머지 하나가 다른 경우
      const p = counts[keys[0]] === 3 ? keys[0] : keys[1];
      const q = counts[keys[0]] === 1 ? keys[0] : keys[1];
      return Math.pow(10 * parseInt(p) + parseInt(q), 2);
    } else {
      // 두 개의 숫자가 각각 두 번씩 나온 경우
      const [p, q] = keys.map(Number);
      return (p + q) * Math.abs(p - q);
    }
  } else if (keys.length === 3) {
    // 두 주사위 숫자가 같고 나머지 두 개가 서로 다른 경우
    for (let key of keys) {
      if (counts[key] === 2) {
        const [q, r] = keys.filter((k) => k !== key).map(Number);
        return q * r;
      }
    }
  } else {
    // 모든 주사위 숫자가 다른 경우
    return Math.min(a, b, c, d);
  }
}
