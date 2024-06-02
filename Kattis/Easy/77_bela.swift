var dominant_values = ["A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0]
var non_dominant_values = ["A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0]

if let input = readLine() {
    let inputs = input.split(separator: " ")
    let n = Int(inputs[0]) ?? 0
    let b = String(inputs[1])
    var count = 0
    
    for _ in 0..<(n*4) {
        if let inp = readLine() {
            let inp = inp.uppercased()
            let a = String(inp.first ?? Character(""))
            let c = String(inp.last ?? Character(""))
            
            if c == b {
                count += dominant_values[a] ?? 0
            } else {
                count += non_dominant_values[a] ?? 0
            }
        }
    }
    
    print(count)
}
