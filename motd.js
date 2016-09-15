var motds = [
"Gotta Go Fast!",
"RIP Harambe 2k16",
"What if the Hokey Cokey really is what it's all about?",
"Can God make a burrito too hot for him to eat?",
"Windows 10 finally added to anti-spyware databases",
"Laplace's daemon summoned from Hell",
"f(x) = f(x + 1)",
"Word of all time: \"Nonplussed\"",
"Copyleft wing or copyright wing?",
"What has hands but no arms and a face but no eyes?",
"The second hand on a clock is either the first or third hand",
"At what angle does the mintue hand cross the hour hand shortly after half past 6?",
"This space intentionally left blank"
];
var bible_books = [
"Genesis",
"Exodus",
"Leviticus",
"Deuteronomy",
"Judges",
"1 Samuel",
"2 Samuel",
"1 Kings",
"2 Kings",
"Ezra",
"Nehemiah",
"Job",
"Psalms",
"Proverbs"
];
var motd = motds[Math.floor(Math.random()*motds.length)];
var bible_book = bible_books[Math.floor(Math.random()*bible_books.length)];
var chapter = Math.floor(Math.random()*20);
var verse = Math.floor(Math.random()*50);
var full = "<p> \"" + motd + "\" " + bible_book + " " + chapter + ":" + verse + "</p>";
document.getElementById("motd").innerHTML = full;


