<script context='module'>
    import { fetchListByID } from '../../stores/lists';
    import { plantList } from '../../stores/plants';

    let listsValue;
    export async function load(ctx) {
        let id = ctx.page.params.id;

        const selectedList = await fetchListByID(id)
        return { props: { selectedList }}
    }
</script>

<script>
    export let selectedList;
</script>

<div class="flex flex-col items-center">
    <h1 class="text-4xl text-center my-8 uppercase">{selectedList.name}</h1>
    {#each selectedList.plants as plant}
    <p class="text">{plant.latin_name}</p>
    {/each}
</div>