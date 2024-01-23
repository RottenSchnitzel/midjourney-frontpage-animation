<script>
	import imageArray from "../lib/logo.txt.json";
	import name from "../lib/name.json";
	import { onMount } from "svelte";

	let animation_index = 0;
	let _array = imageArray[animation_index];
	let showInput = true;
	let inputElement;
	let inputValue = "";
	let isFlipped = false;
	
	const inputPrompt = '<div style="color: rgba(255,161,1,255);">guest</div><div style="color: grey;">@</div><div style="color: rgba(80,126,255,255);">alcedo.digital</div><div style="color: grey">&nbsp;~>&nbsp;</div>';
	
	let stdout = [];
	let history = [];

	let historyCursor = 0;

	const addLine = async (text) => {
		stdout = [...stdout, text];
	};

	const onKey = (e) => {
		let key = e.key;
		if (key === 'ArrowUp') {
			inputValue = history[historyCursor];
			++historyCursor;
		}
		if (key === 'ArrowDown' && historyCursor > 0) {
			--historyCursor;
			inputValue = history[historyCursor];
		}
	}

	const printHelp = () => {
		addLine("<br>");
		addLine("Useful commands: <br><br>");
		addLine("help");
		addLine("contact");
		addLine("about");
		addLine("projects");
		addLine("vim");
		addLine("<br>");
	}

	const clear = () => {
		stdout = [];
	}

	const onInput = () => {
		let terminal = document.getElementById("terminal");
		addLine(inputPrompt + inputValue);
		history = [inputValue, ...history];
		showInput = false;
		if (inputValue === "help") {
			printHelp();
		} else if (inputValue === "clear") {
			clear();
		} else if (inputValue === "hostname") {
			addLine("alcedo.digital");
		} else if (inputValue === "vim") {
			window.open("https://youtu.be/2qBlE2-WL60");
		} else if (inputValue === "contact") {
			addLine("Phone Number: " + "+4367761" + "806791");
			addLine("Email: " + "contact" + "@" + "alcedo" + ".digital");
		} else if (inputValue === "about") {
			addLine("<br>");
			addLine("We are crafting code with passion!");
			addLine("<br>");
			addLine("At Alcedo Digital, we specialize in an array of services that cater to your digital requirements:");
			addLine("Frontend Development  Web Development  Backend Development  Mobile Apps");
			addLine("<br>");
		} else if (inputValue === "ls") {
			addLine("homework  projects  images");
		} else if (inputValue === "projects") {
			addLine("domalio.com (in development)  sk-as.at (in development)");
		} else if (inputValue === "flip") {
			if (isFlipped) {
				isFlipped = false;
				terminal.style = "";
			} else {
				isFlipped = true;
				terminal.style = "transform: rotate(180deg);";
			}
		} else if (inputValue === "") {
			
		} else if (inputValue === "") {
			
		} else if (inputValue === "") {
			
		} else if (inputValue === "") {
			
		} else {
			addLine(inputValue + ": " + "command not found")
		}
		inputValue = "";
		showInput = true;
		terminal.scrollTo(0, terminal.scrollHeight);
	};

	onMount(() => {
		inputElement = document.getElementById("input");
		addLine("Welcome to alcedo.digital!<br><br>");
		name.forEach(e => {
			addLine(e);
		});
		addLine("<br>");
		addLine('Type in "help" to get a list of useful commands<br><br>');
		/*let interval = setInterval(() => {
			animation_index += 1;
			if (animation_index < 400) {
				_array = imageArray[400 - animation_index];
			} else {
				clearInterval(interval);
			}
		}, 10);*/
	});

</script>

<!--div class="top">
	{#if _array}
		<pre class="projection" id="projection">
			{@html _array}
		</pre>
	{/if}
</div-->
<div class="terminal" id="terminal" on:mouseup={() => {inputElement.focus()}}>
	{#each stdout as line}
		<div class="line">
			{@html line}
		</div>
	{/each}
	{#if showInput}
		<form on:submit|preventDefault={onInput}>
			<div class="line">
				<div class="input">
					{@html inputPrompt}
					<input type="text" bind:value={inputValue} id="input" autofocus autocomplete="off" on:keydown={onKey}/>
				</div>
			</div>
		</form>
	{/if}
</div>

<style>
	.terminal {
		overflow-y: scroll;
		z-index: 10;
		flex: 1;
		background-color: rgb(49, 49, 49);
		border: 2px solid rgba(80,126,255,255);
		padding: 20px;
	}
	.terminal::-webkit-scrollbar {
		display: none;
	}
	pre {
		all: inherit;
	}
	.line {
		display: flex;
		white-space: pre;
	}
	.input {
		display: flex;
	}
	input {
		background-color: transparent;
		border: none;
		all: unset;
	}
	.projection {
		position: absolute;
		top: 0;
		left: 0;
		width: 100px;
		height: 100px;
		font-weight: 400;
		font-size: 5px;
		line-height: 5px;
		overflow: hidden;
	}
</style>
