export interface Editora {
    id: number;
    editora: string; 
    cnpj?: string | null;
    endereco: string;
    telefone?: string | null;
    email?: string | null;
    site?: string | null;
} 


/*
editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True)    
    endereco = models.CharField(max_length=200, null=True, blank=True) 
    telefone = models.CharField(max_length=20, null=True, blank=True) 
    email = models.EmailField(null=True, blank=True) 
    site = models.URLField(null=True, blank=True)


*/