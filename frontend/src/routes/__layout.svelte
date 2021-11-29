<nav class="bg-gray-800 flex items-center h-16">
	<a class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium" href="/">Home</a>
	<a class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium" href="/test">Teszt</a>
	<a class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium" href="/lists">Listák</a>
	<a class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium" href="/plants">Növények</a>
	<a class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium" href="/upload">Feltöltés</a>
</nav>

<slot></slot>

<style>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>