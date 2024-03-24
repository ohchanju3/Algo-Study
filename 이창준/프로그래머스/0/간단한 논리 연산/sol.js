function solution(x1, x2, x3, x4) {
  // (x1 ∨ x2) ∧ (x3 ∨ x4) 식 계산
  var result = (x1 || x2) && (x3 || x4);
  return result;
}
