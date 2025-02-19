table = [137100, 213480, 377700] //How many seconds for every lesson since monday

//returns first current week's monday's 0:00am
function BeginningOfWeek(CurrentUnixTime){
    return CurrentUnixTime-((CurrentUnixTime - 345600)%604800) //equation
}

//time is the seconds since beginning of week
function returnNextLesson(SecSinceBeginning){
    for (let index = 0; index < table.length; index++) {
        if (SecSinceBeginning < table[index]){
            
            console.log(index)
            return table[index]
        }
        return 604800 + table[0] //next week's first lesson
    }
}

//calculates how long left for the next lesson
function howLongTo(nextLesson){
    let timeDifference = nextLesson;
    let timeParts = [];
    
    const days = Math.floor(timeDifference / (60 * 60 * 24));
    const hours = Math.floor((timeDifference / (60 * 60)) % 24);
    const minutes = Math.floor((timeDifference / 60) % 60);
    const seconds = Math.floor(timeDifference % 60);
    
    if (timeDifference < 0) {
        timeDifference = Math.abs(timeDifference);
        
        if (days > 0) timeParts.push(`${days} days`);
        if (hours > 0) timeParts.push(`${hours} hours`);
        if (minutes > 0) timeParts.push(`${minutes} minutes`);
        if (seconds > 0) timeParts.push(`${seconds} seconds`);
        
        return timeParts.length ? timeParts.join(", ") + " ago" : "Just now";
    } else {
        if (days > 0) timeParts.push(`${days} days`);
        if (hours > 0) timeParts.push(`${hours} hours`);
        if (minutes > 0) timeParts.push(`${minutes} minutes`);
        if (seconds > 0) timeParts.push(`${seconds} seconds`);
        
        return timeParts.length ? "In " + timeParts.join(", ") : "Now";
    }
}

//this is the function that will execute everything. Tried to make it look similar to C++ haha 👏👏👏
function main(){
    //variables that calculates the next lesson
    var CurrUnixTime = Math.floor(Date.now()/1000)
    var WeekBegin = BeginningOfWeek(CurrUnixTime)
    var nextLessonValue = returnNextLesson(CurrUnixTime - WeekBegin)
    var nextLessonUnix = WeekBegin + nextLessonValue

    //convert to Australian Timezone (NON-DAYLIGHT)
    nextLessonUnix -= 36000
    
    console.clear()
    console.log(`Next Lesson in at Unix Time: ${nextLessonUnix}`)
    console.log(`Next Lesson: ${howLongTo(nextLessonUnix-CurrUnixTime)}`)
}

var repeatMain = setInterval(main, 1000);