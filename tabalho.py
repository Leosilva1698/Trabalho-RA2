def inicialziar_cache(tamanho_cache):
    memoria_cache = {}
    
    for i in range(tamanho_cache):
        memoria_cache[i] = -1

    return memoria_cache
    
def imprimir_cache(cache):
    for key in dict.keys(cache):
        print('|',key, '|' , cache[key],'|')


def mapemanto_direto(tamanho_cache, pos_memoria):
    miss = 0
    hit = 0
    cache = inicialziar_cache(tamanho_cache)
    imprimir_cache(cache)

    for i in pos_memoria:
        posicao_cahe = i % tamanho_cache
        if cache[posicao_cahe] != i:
            cache[posicao_cahe] = i
            print('Miss')
            miss += 1   
        else:
            print('Hit')
            hit += 1   
        imprimir_cache(cache)
    print('Total de posiocoes acessadas:', len(pos_memoria))
    print('Total de hits:', hit)
    print('Total de miss:', miss)
    print('Taxa de hit:', hit/len(pos_memoria))
    print('Taxa de miss:', miss/len(pos_memoria))

def main():
    tamanho_cache = 20
    pos_memoria = [52,46, 63, 46, 50]
    mapemanto_direto(tamanho_cache, pos_memoria)

main()
