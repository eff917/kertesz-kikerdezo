<script>
import { plantData } from '../../stores/plants';
let plantsValue;
plantData.subscribe((values) => {
    plantsValue = values
});
let plants = [];
</script>

<h2 class="text-4xl text-center my-8 uppercase">Új növény feltöltése</h2>
<form class="text-center" action="/api/plants" enctype="multipart/form-data" method="post">
    <label for="files">Képek</label>
    <input class="my-2 border-2 border-black rounded" name="files" type="file" multiple><br />
    <label for="latinName">Latin név</label>
    <input class="my-2 border-2 border-black rounded" name="latinName" type="text"><br />
    <label for="hungarianName">Magyar név</label>
    <input class="my-2 border-2 border-black rounded" name="hungarianName" type="text"><br />
    <input class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit" value="Feltöltés">
</form>

<h2 class="text-4xl text-center my-8 uppercase">Új lista létrehozása</h2>
<form class="text-center" action="/api/lists" enctype="application/json" method="post">
    <label for="name">Lista neve</label>
    <input class="my-2 border-2 border-black rounded" name="name" type="text"><br />
    <div class="grid md:grid-cols-2 lg:grid-cols-3">
    {#each plantsValue as plant}
        <div class="grid grid-cols-2">
        <div class="text-right m-5">
        <input type="checkbox" bind:group={plants} id="{plant.id}" name="plants" value={plant.id}>
        </div>
        <div class="grid grid-cols-1 text-left">
        <label for="{plant.id}">{plant.latin_name}</label>
        <label for="{plant.id}">{plant.hungarian_name}</label>
        </div>
        </div>
    {/each}
    </div>
    <input class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit" value="Feltöltés">
</form>
