<script context='module'>
    import { fetchPlantByID } from '../../stores/plants';

    let listsValue;
    export async function load(ctx) {
        let id = ctx.page.params.id;

        const selectedList = await fetchPlantByID(id)
        return { props: { selectedPlant }}
    }
</script>

<script>
    export let selectedPlant;
</script>

<div class="flex flex-col items-center">
    <h1 class="text-4xl text-center my-8 uppercase">{selectedPlant.latin_name}</h1>
    {#each selectedPlant.pictures as picture}
    <p class="text">{picture}</p>
    {/each}
</div>