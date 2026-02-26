import os

def print_environment_variables(search_term=None):
    """
    Print all environment variables, optionally filtering by search term
    
    Args:
        search_term: Optional string to filter variables (case insensitive)
    """
    env_vars = dict(os.environ)
    
    if search_term:
        search_term = search_term.lower()
        filtered_vars = {k: v for k, v in env_vars.items() 
                        if search_term in k.lower() or search_term in str(v).lower()}
        print(f"Found {len(filtered_vars)} environment variables containing '{search_term}':\n")
        env_vars = filtered_vars
    else:
        print(f"All environment variables ({len(env_vars)} total):\n")
    
    for key in sorted(env_vars.keys()):
        print(f"{key}: {env_vars[key]}")

# Usage
print_environment_variables() 
# print_environment_variables("path")  # Print only those containing "path"
# print_environment_variables("python")  # Print only those containing "python"