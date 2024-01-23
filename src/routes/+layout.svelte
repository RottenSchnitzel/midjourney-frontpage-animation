<script>
	import "@fontsource/roboto-mono";
</script>

<slot></slot>

<style>
	:global(body) {
		font-family: "Roboto Mono", monospace;
		padding: 20px;
		line-height: 20px;
		margin: 0;
		height: calc(100% - 40px);
		color: white;
		display: flex;
		align-items: stretch;
		background-color: rgb(37, 37, 37);
	}
	:global(html) {
		padding: 0;
		margin: 0;
		height: 100%;
		width: 100%;
	}
</style>