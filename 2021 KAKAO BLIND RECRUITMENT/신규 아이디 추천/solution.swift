import Foundation

func solution(_ new_id:String) -> String {
    var answer:String = ""
    
    //Step 1, 2
    var temp:String = ""
    for index in new_id.indices {
        if(new_id[index].isLetter){
            temp.append(new_id[index].lowercased())
        }
        if(new_id[index].isNumber){
            temp.append(new_id[index])
        }
        if(new_id[index] == "-" || new_id[index] == "_" || new_id[index] == "."){
            temp.append(new_id[index])
        }
    }
    answer = temp
    print(answer)
    
    //Step 3
    temp = ""
    var prev:Bool = false
    for index in answer.indices {
        if(answer[index] == "."){
            if(prev == true){
                continue
            }
            temp.append(answer[index])
            prev = true
        }
        else{
            temp.append(answer[index])
            prev = false
        }
    }
    answer = temp
    print(answer)

    //Step 4
    if(!answer.isEmpty){
        if(answer[answer.startIndex] == "."){
            answer.remove(at:answer.startIndex)
        }
    }
    if(!answer.isEmpty){
        if(answer[answer.index(before: answer.endIndex)] == "."){
            answer.remove(at:answer.index(before: answer.endIndex))
        }
    }
    print(answer)
    //Step 5
    if(answer.isEmpty){
        answer.append("a")
    }
    print(answer)
    //Step 6
    if(answer.count >= 16){
        let range = answer.index(answer.startIndex, offsetBy: 15)..<answer.endIndex
        answer.removeSubrange(range)
    }
    if(answer[answer.index(before: answer.endIndex)] == "."){
        answer.remove(at:answer.index(before: answer.endIndex))
    }
    print(answer)
    //Step 7
    if(answer.count <= 2){
        while(answer.count <= 2){
            answer.append(answer[answer.index(before: answer.endIndex)])
        }
    }
    print(answer)
    return answer
}
