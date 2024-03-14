function solution(arr, idx) {
  let smallestIndex = Infinity;
  for (let i = idx + 1; i < arr.length; i++) {
    if (arr[i] === 1) {
      smallestIndex = Math.min(smallestIndex, i);
    }
  }
  return smallestIndex === Infinity ? -1 : smallestIndex;
}
