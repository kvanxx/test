function isPalindrome(str) {

  var cleaned = str.replace(/[\W_]/g, '').toLowerCase();

  return cleaned === cleaned.split('').reverse().join('');
}