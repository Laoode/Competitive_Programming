let n = Int(readLine()!)!

var kombinasi: [[Int]] = []
var frekuensi: [Int] = []

for _ in 0..<n {
    let line = readLine()!.split(separator: " ").map { Int($0)! }
    let m = line.sorted()

    var found = false
    for i in 0..<kombinasi.count {
        if kombinasi[i] == m {
            frekuensi[i] += 1
            found = true
            break
        }
    }

    if !found {
        kombinasi.append(m)
        frekuensi.append(1)
    }
}

var maks = 0
for f in frekuensi {
    if f > maks {
        maks = f
    }
}

var hasil = 0
for f in frekuensi {
    if f == maks {
        hasil += f
    }
}

print(hasil)