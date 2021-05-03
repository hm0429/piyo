const crypto = require('crypto')

// 配列のサイズ
const N = 100 

// UInt16 なので、取りうる値の範囲は 0 ~ 65535
const baseArray = new Uint16Array(N)

let loopCount = 0

function bubbleSort(arr) {
	// 配列は参照渡しのため、コピーして使う
	let a = [...arr]

	// ソート完了のフラグ
	let sorted = false
	while (sorted == false) {
		// 以下の for ループ中で順番がおかしくなければ
		// sorted フラグが true のままになるので、
		// while ループを抜ける
		sorted = true

		// 配列を先頭から順番にチェックしていく
		for (let i = 0; i < a.length - 1; i++) {
			// 順番がおかしければ swap
			if (a[i] > a[i+1]) {
				let tmp = a[i]
				a[i] = a[i+1]
				a[i+1] = tmp
				sorted = false
			}
			loopCount++
		}
	} 
	return a
}

function main() {
	// sort する対象の配列を作成
	const input = crypto.randomFillSync(baseArray)
	console.log(`input: ${input}`)

	const output = bubbleSort(input)
	console.log(`output: ${output}`)

	console.log(`loopCount: ${loopCount}`)
}

main()