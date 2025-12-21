"""
Analysis and Visualization Tools for Prime Synchronization Theorem
Statistical analysis and result validation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.model_selection import KFold
import warnings
warnings.filterwarnings('ignore')

def cross_validate_scaling(N_values, kappa_c_values, gamma_values, n_folds=5):
    """
    Perform k-fold cross-validation of scaling law.
    
    Parameters:
    -----------
    N_values : array-like
        Array of N values
    kappa_c_values : array-like
        Critical coupling values
    gamma_values : array-like
        Goldbach sums
    n_folds : int
        Number of folds for cross-validation
    
    Returns:
    --------
    results : dict
        Cross-validation results
    """
    X = np.log(np.array(N_values)).reshape(-1, 1)
    y = np.log(np.array(kappa_c_values) * np.array(gamma_values))
    
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)
    
    fold_results = {
        'fold': [],
        'a': [],
        'b': [],
        'rmse': [],
        'r2': []
    }
    
    for fold, (train_idx, test_idx) in enumerate(kf.split(X)):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        
        # Linear fit in log-log space: log(y) = log(a) + b*log(N)
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            X_train.flatten(), y_train
        )
        
        a = np.exp(intercept)  # Convert back from log space
        b = slope
        
        # Predict on test set
        y_pred = intercept + slope * X_test.flatten()
        y_pred_original = np.exp(y_pred)
        y_test_original = np.exp(y_test)
        
        # Calculate metrics
        rmse = np.sqrt(np.mean((y_pred_original - y_test_original)**2))
        ss_res = np.sum((y_test - y_pred)**2)
        ss_tot = np.sum((y_test - np.mean(y_test))**2)
        r2 = 1 - (ss_res / ss_tot)
        
        fold_results['fold'].append(fold + 1)
        fold_results['a'].append(a)
        fold_results['b'].append(b)
        fold_results['rmse'].append(rmse)
        fold_results['r2'].append(r2)
    
    return fold_results

def statistical_analysis():
    """
    Perform comprehensive statistical analysis.
    Based on Table 1 from the paper.
    """
    # Data from Table 1 (N, π(N), κ_c, Γ, κ_c·Γ, κ_c/ΔΩ)
    data = {
        'N': [30, 50, 100, 200, 300, 500, 700, 1000],
        'pi_N': [10, 15, 25, 46, 62, 95, 125, 168],
        'kappa_c': [174.2, 273.4, 315.6, 434.4, 515.6, 715.6, 892.4, 1128.6],
        'gamma': [0.4431, 0.5843, 0.7283, 0.8261, 0.8673, 0.9023, 0.9382, 0.9621],
        'product': [77.2, 159.8, 229.9, 358.8, 447.2, 645.8, 837.1, 1085.4],
        'kappa_over_delta': [64.3, 84.9, 80.7, 94.2, 102.9, 129.6, 158.7, 194.3]
    }
    
    df = pd.DataFrame(data)
    
    print("=" * 80)
    print("STATISTICAL ANALYSIS OF PRIME SYNCHRONIZATION THEOREM")
    print("=" * 80)
    
    # 1. Fit scaling law: κ_c·Γ = A·N^b
    log_N = np.log(df['N'])
    log_product = np.log(df['product'])
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(log_N, log_product)
    
    A = np.exp(intercept)
    b = slope
    r2 = r_value**2
    
    print("\n1. SCALING LAW FIT:")
    print("-" * 40)
    print(f"   Equation: κ_c(N)·Γ(N) = A·N^b")
    print(f"   Fitted:   A = {A:.4f}, b = {b:.4f}")
    print(f"   Original: A = 2.539,  b = 0.9327")
    print(f"   R² = {r2:.6f}, p-value = {p_value:.2e}")
    print(f"   Standard error: {std_err:.6f}")
    
    # 2. Cross-validation
    print("\n2. CROSS-VALIDATION (5-fold):")
    print("-" * 40)
    
    cv_results = cross_validate_scaling(
        df['N'], df['kappa_c'], df['gamma'], n_folds=5
    )
    
    cv_df = pd.DataFrame(cv_results)
    print(cv_df.to_string(index=False))
    
    print(f"\n   Average R²: {cv_df['r2'].mean():.6f}")
    print(f"   Average RMSE: {cv_df['rmse'].mean():.2f}")
    
    # 3. κ_c/ΔΩ linear fit
    print("\n3. κ_c/ΔΩ SCALING BARRIER ANALYSIS:")
    print("-" * 40)
    
    slope_kappa, intercept_kappa, r_kappa, p_kappa, _ = stats.linregress(
        df['N'], df['kappa_over_delta']
    )
    
    print(f"   Linear fit: κ_c/ΔΩ = {intercept_kappa:.1f} + {slope_kappa:.3f}·N")
    print(f"   R² = {r_kappa**2:.3f}, p-value = {p_kappa:.2e}")
    print(f"   At N=30: predicted = {intercept_kappa + slope_kappa*30:.1f}, actual = {df['kappa_over_delta'].iloc[0]:.1f}")
    print(f"   At N=1000: predicted = {intercept_kappa + slope_kappa*1000:.1f}, actual = {df['kappa_over_delta'].iloc[-1]:.1f}")
    
    # 4. Statistical tests
    print("\n4. STATISTICAL SIGNIFICANCE TESTS:")
    print("-" * 40)
    
    # Test if scaling law parameters match theoretical values
    t_stat_A = (A - 2.539) / (std_err / np.sqrt(len(df)))
    t_stat_b = (b - 0.9327) / (std_err / np.sqrt(len(df)))
    
    df_t = len(df) - 2  # degrees of freedom
    p_A = 2 * (1 - stats.t.cdf(np.abs(t_stat_A), df_t))
    p_b = 2 * (1 - stats.t.cdf(np.abs(t_stat_b), df_t))
    
    print(f"   Test A = 2.539: t = {t_stat_A:.3f}, p = {p_A:.4f}")
    print(f"   Test b = 0.9327: t = {t_stat_b:.3f}, p = {p_b:.4f}")
    
    if p_A > 0.05 and p_b > 0.05:
        print("   Conclusion: No significant difference from theoretical values (p > 0.05)")
    else:
        print("   Conclusion: Significant difference from theoretical values (p < 0.05)")
    
    # 5. Create comprehensive visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Scaling law
    N_fine = np.linspace(30, 1000, 100)
    axes[0, 0].plot(df['N'], df['product'], 'ro', markersize=8, label='Data')
    axes[0, 0].plot(N_fine, A * (N_fine**b), 'b-', linewidth=2, 
                    label=f'Fit: {A:.3f}·N^{b:.4f}')
    axes[0, 0].plot(N_fine, 2.539 * (N_fine**0.9327), 'g--', linewidth=2,
                    label='Theory: 2.539·N^0.9327')
    axes[0, 0].set_xlabel('N', fontsize=12)
    axes[0, 0].set_ylabel('κ_c·Γ(N)', fontsize=12)
    axes[0, 0].set_title('Scaling Law Verification', fontsize=14)
    axes[0, 0].legend(fontsize=10)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xscale('log')
    axes[0, 0].set_yscale('log')
    
    # Plot 2: κ_c/ΔΩ scaling
    axes[0, 1].plot(df['N'], df['kappa_over_delta'], 'bo-', linewidth=2, markersize=6)
    axes[0, 1].plot(N_fine, intercept_kappa + slope_kappa * N_fine, 'r--', 
                    linewidth=2, label='Linear fit')
    axes[0, 1].set_xlabel('N', fontsize=12)
    axes[0, 1].set_ylabel('κ_c/ΔΩ', fontsize=12)
    axes[0, 1].set_title('κ_c/ΔΩ Scaling Barrier', fontsize=14)
    axes[0, 1].legend(fontsize=10)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Residuals
    predicted = A * (df['N']**b)
    residuals = df['product'] - predicted
    axes[1, 0].plot(df['N'], residuals, 'go', markersize=8)
    axes[1, 0].axhline(y=0, color='r', linestyle='--', alpha=0.5)
    axes[1, 0].set_xlabel('N', fontsize=12)
    axes[1, 0].set_ylabel('Residuals', fontsize=12)
    axes[1, 0].set_title('Scaling Law Residuals', fontsize=14)
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Cross-validation results
    fold_numbers = cv_df['fold']
    r2_values = cv_df['r2']
    axes[1, 1].bar(fold_numbers, r2_values, color='skyblue', alpha=0.7)
    axes[1, 1].axhline(y=np.mean(r2_values), color='r', linestyle='--', 
                       linewidth=2, label=f'Mean: {np.mean(r2_values):.4f}')
    axes[1, 1].set_xlabel('Fold Number', fontsize=12)
    axes[1, 1].set_ylabel('R²', fontsize=12)
    axes[1, 1].set_title('Cross-Validation Results', fontsize=14)
    axes[1, 1].legend(fontsize=10)
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    axes[1, 1].set_ylim([0.999, 1.001])
    
    plt.tight_layout()
    plt.savefig('statistical_analysis.png', dpi=150)
    plt.show()
    
    print("\n" + "=" * 80)
    print("Analysis complete. Results saved to 'statistical_analysis.png'")
    print("=" * 80)
    
    return df, cv_df

def main():
    """Run the complete analysis."""
    df, cv_df = statistical_analysis()
    
    # Save results to CSV
    df.to_csv('simulation_results.csv', index=False)
    cv_df.to_csv('cross_validation_results.csv', index=False)
    
    print("\nData saved to:")
    print("  - simulation_results.csv")
    print("  - cross_validation_results.csv")

if __name__ == "__main__":
    main()