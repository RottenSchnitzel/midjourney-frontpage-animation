<script>
	import imageMatrix from "../lib/out.json";
	import alcedoMatrix from "../lib/alcedo.json";

	export let rows = 75;
	export let cols = 150;

	let _matrix = imageMatrix[0];
	let randomArray = getRandomArray(rows, 0, 4);
	let randomArray2 = getRandomArray(rows, 0, 1);
	let color = new Array(rows).fill(new Array(cols));

	let matrix = new Array(rows).fill(
		'#include<stdio.h>int main(){int n,i;long long int fib[50];printf("Input:");scanf("%d",&n);fib[0]=0;fib[1]=1;for(i=2;i<n;i++){fib[i]=fib[i-1]+fib[i-2];}printf("Series:");for(i=0;i<n;i++){printf("%lld",fib[i]);}return 0;}#include<stdio.h>int main(){int n,i;long long int fib[50];printf("Input:");scanf("%d",&n);fib[0]=0;fib[1]=1;for(i=2;i<n;i++){fib[i]=fib[i-1]+fib[i-2];}printf("Series:");for(i=0;i<n;i++){printf("%lld",fib[i]);}return 0;}'
	);

	for (let i = 1; i < matrix.length; i++) {
		matrix[i] = matrix[i].slice(i + randomArray[i]);
		for (let j = 0; j < cols; j++) {
			color[i][j] = Math.floor(Math.random() * 3);
		}
	}

	let animation_index = 1;

	function rotateFigure(matrix, degrees) {
		const radians = (degrees * Math.PI) / 180;
		const cosRadians = Math.cos(radians);
		const sinRadians = Math.sin(radians);
		const centerX = matrix.length / 2;
		const centerY = matrix[0].length / 2;

		const rotatedMatrix = [];

		for (let i = 0; i < matrix.length; i++) {
			rotatedMatrix[i] = [];
			const x = i - centerX;

			for (let j = 0; j < matrix[i].length; j++) {
				const y = j - centerY;

				const rotatedX =
					Math.round(x * cosRadians - y * sinRadians) + centerX;
				const rotatedY =
					Math.round(x * sinRadians + y * cosRadians) + centerY;

				rotatedMatrix[i][j] =
					rotatedX >= 0 &&
					rotatedX < matrix.length &&
					rotatedY >= 0 &&
					rotatedY < matrix[i].length
						? matrix[rotatedX][rotatedY]
						: false;
			}
		}

		return rotatedMatrix;
	}

	function getRandomArray(length, min, max) {
		var arr = [];
		for (var i = 0; i < length; i++) {
			arr.push(Math.floor(Math.random() * (max - min + 1)) + min);
		}
		return arr;
	}

	const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

	let flag = false;

	function shiftMatrix(matrix) {
		for (let i = 0; i < matrix.length; i++) {
			/*if (
				(randomArray2[i] == 0 && flag) ||
				(randomArray2[i] == 1 && !flag)
			)*/
				let string = matrix[i];
				let stringArray = string.split("");
				stringArray[Math.floor(Math.random() * stringArray.length)] = String.fromCharCode(Math.floor(Math.random() * (127 - 32)) + 32);
				matrix[i] = stringArray.join("");
		}

		return matrix;
	}

	setInterval(() => {
		_matrix = imageMatrix[animation_index];
		animation_index++;
		if (animation_index >= 180) {
			animation_index = 0;
		}
	}, 50);

	console.log(matrix.length);

	setInterval(() => {
		matrix = shiftMatrix(matrix, 1);
		flag = !flag;
	}, 1);
</script>

<div class="projection" id="projection">
	{#each matrix as row, i}
		<div class="row">
			{#each row as col, j}
				{#if j <= 150}
					<div class={alcedoMatrix[i][j] || j > 130 ? "col" : "col logo"}>
						<!--{matrix[i][j]}-->
						{@html _matrix[Math.floor(i / 2)][Math.floor(j / 2)] ||
						!alcedoMatrix[i][j]
							? matrix[i][j]
							: "&nbsp;"}
					</div>
				{/if}
			{/each}
		</div>
	{/each}
</div>
<style>
	.projection {
		width: 80vw;
		height: 80vh;
		font-weight: 600;
		overflow: hidden;
		margin: 10vh auto;
	}
	.row {
		display: flex;
		flex-direction: row;
		height: calc(80vh / 75);
	}
	.col {
		font-size: 9px;
		width: calc(80vw / 150);
		color: #5981fb;
	}
	.logo {
		color: white;
	}
</style>
