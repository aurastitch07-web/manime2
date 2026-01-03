"""Maximum likelihood demonstrations animated in a 3Blue1Brown style."""

from manim import *

config.quality = "high_quality"
config.background_color = "#1e1e1e"

__all__ = ["EMV"]


class EMV(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"

        self.normal_section()
        self.clear()
        self.poisson_section()
        self.clear()
        self.bernoulli_section()
        self.clear()
        self.uniform_section()

    def normal_section(self):
        title = Tex(r"Loi Normale $N(\mu, \sigma^2)$", font_size=48)
        title.set_color_by_tex(r"\mu", YELLOW)
        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP))

        likelihood = MathTex(
            r"L(", r"\mu", r")", r"=", r"\prod_{i=1}^n", r"f(", r"x_i", r")",
            r"=", r"\left(\frac{1}{\sigma\sqrt{2\pi}}\right)^n",
            r"\exp\left(-\frac{\sum_{i=1}^n(x_i-\mu)^2}{2\sigma^2}\right)",
            font_size=42,
        )
        likelihood.set_color_by_tex(r"\mu", YELLOW)
        likelihood.set_color_by_tex(r"x_i", BLUE)
        self.play(Write(likelihood))

        log_wrap = MathTex(
            r"\ln(L(", r"\mu", r"))", r"=", r"\ln\Big[",
            r"\left(\frac{1}{\sigma\sqrt{2\pi}}\right)^n",
            r"\exp\left(-\frac{\sum(x_i-\mu)^2}{2\sigma^2}\right)",
            r"\Big]",
            font_size=42,
        )
        log_wrap.set_color_by_tex(r"\mu", YELLOW)
        log_wrap.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                likelihood.copy(),
                log_wrap,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        log_simplified = MathTex(
            r"\ln L(", r"\mu", r")", r"=", r"\text{Constante}",
            r"-", r"\frac{1}{2\sigma^2}", r"\sum_{i=1}^n(x_i-\mu)^2",
            font_size=42,
        )
        log_simplified.set_color_by_tex(r"\mu", YELLOW)
        log_simplified.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                log_wrap,
                log_simplified,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        deriv_label = MathTex(r"\frac{\partial}{\partial \mu}\ln L(\mu)", font_size=42)
        deriv_label.set_color_by_tex(r"\mu", YELLOW)
        box = SurroundingRectangle(log_simplified, color=GREEN)
        self.play(Create(box))
        self.play(log_simplified.animate.shift(UP * 0.5), FadeOut(box))
        self.play(Write(deriv_label.next_to(log_simplified, DOWN)))

        derivative = MathTex(
            r"\frac{\partial \ln L}{\partial \mu}", r"=",
            r"\frac{1}{\sigma^2}\sum_{i=1}^n(x_i-\mu)",
            font_size=42,
        )
        derivative.set_color_by_tex(r"\mu", YELLOW)
        derivative.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                log_simplified,
                derivative,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=3,
            )
        )

        set_zero = MathTex(
            r"\sum_{i=1}^n x_i - n\mu = 0",
            font_size=42,
        )
        set_zero.set_color_by_tex(r"\mu", YELLOW)
        set_zero.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                derivative,
                set_zero,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        mu_hat = MathTex(
            r"\hat{\mu}", r"=", r"\frac{1}{n}\sum_{i=1}^n x_i", r"=", r"\bar{X}",
            font_size=42,
        )
        mu_hat.set_color_by_tex(r"\mu", YELLOW)
        mu_hat.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                set_zero,
                mu_hat,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        second_deriv = MathTex(
            r"\frac{\partial^2 \ln L}{\partial \mu^2}", r"=", r"-\frac{n}{\sigma^2} < 0",
            font_size=42,
        )
        second_deriv.set_color_by_tex(r"\mu", YELLOW)
        self.play(
            TransformMatchingTex(
                mu_hat.copy(),
                second_deriv,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )
        self.play(FadeOut(second_deriv), FadeOut(mu_hat), FadeOut(title))

    def poisson_section(self):
        title = Tex(r"Loi de Poisson $(\lambda)$", font_size=48)
        title.set_color_by_tex(r"\lambda", YELLOW)
        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP))

        likelihood = MathTex(
            r"L(", r"\lambda", r")", r"=", r"\prod_{i=1}^n", r"e^{-\lambda}", r"\frac{\lambda^{x_i}}{x_i!}",
            r"=", r"e^{-n\lambda}", r"\frac{\lambda^{\sum x_i}}{\prod x_i!}",
            font_size=42,
        )
        likelihood.set_color_by_tex(r"\lambda", YELLOW)
        likelihood.set_color_by_tex(r"x_i", BLUE)
        self.play(Write(likelihood))

        log_wrap = MathTex(
            r"\ln(L(", r"\lambda", r"))", r"=", r"\ln\Big[",
            r"e^{-n\lambda}", r"\frac{\lambda^{\sum x_i}}{\prod x_i!}",
            r"\Big]",
            font_size=42,
        )
        log_wrap.set_color_by_tex(r"\lambda", YELLOW)
        log_wrap.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                likelihood.copy(),
                log_wrap,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        log_simplified = MathTex(
            r"\ln L(", r"\lambda", r")", r"=", r"-n\lambda", r"+", r"\left(\sum x_i\right)", r"\ln(\lambda)",
            r"-", r"\ln\Big(\prod x_i!\Big)",
            font_size=42,
        )
        log_simplified.set_color_by_tex(r"\lambda", YELLOW)
        log_simplified.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                log_wrap,
                log_simplified,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        derivative = MathTex(
            r"\frac{\partial \ln L}{\partial \lambda}", r"=", r"-n", r"+", r"\frac{\sum x_i}{\lambda}",
            font_size=42,
        )
        derivative.set_color_by_tex(r"\lambda", YELLOW)
        derivative.set_color_by_tex(r"x_i", BLUE)
        highlight = SurroundingRectangle(log_simplified, color=GREEN)
        self.play(Create(highlight))
        self.play(
            TransformMatchingTex(
                log_simplified,
                derivative,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=3,
            )
        )
        self.play(FadeOut(highlight))

        set_zero = MathTex(
            r"n = \frac{\sum x_i}{\lambda}",
            font_size=42,
        )
        set_zero.set_color_by_tex(r"\lambda", YELLOW)
        set_zero.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                derivative,
                set_zero,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        lambda_hat = MathTex(
            r"\hat{\lambda}", r"=", r"\frac{1}{n}\sum x_i", r"=", r"\bar{X}",
            font_size=42,
        )
        lambda_hat.set_color_by_tex(r"\lambda", YELLOW)
        lambda_hat.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                set_zero,
                lambda_hat,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        second_deriv = MathTex(
            r"\frac{\partial^2 \ln L}{\partial \lambda^2} = -\frac{\sum x_i}{\lambda^2} < 0",
            font_size=42,
        )
        second_deriv.set_color_by_tex(r"\lambda", YELLOW)
        second_deriv.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                lambda_hat.copy(),
                second_deriv,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )
        self.play(FadeOut(second_deriv), FadeOut(lambda_hat), FadeOut(title))

    def bernoulli_section(self):
        title = Tex(r"Loi de Bernoulli $(p)$", font_size=48)
        title.set_color_by_tex(r"p", YELLOW)
        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP))

        likelihood = MathTex(
            r"L(", r"p", r")", r"=", r"\prod_{i=1}^n", r"p^{x_i}", r"(1-p)^{1-x_i}",
            r"=", r"p^{\sum x_i}", r"(1-p)^{n-\sum x_i}",
            font_size=42,
        )
        likelihood.set_color_by_tex(r"p", YELLOW)
        likelihood.set_color_by_tex(r"x_i", BLUE)
        self.play(Write(likelihood))

        log_wrap = MathTex(
            r"\ln(L(", r"p", r"))", r"=", r"\ln\Big[p^{\sum x_i}(1-p)^{n-\sum x_i}\Big]",
            font_size=42,
        )
        log_wrap.set_color_by_tex(r"p", YELLOW)
        log_wrap.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                likelihood.copy(),
                log_wrap,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        log_simplified = MathTex(
            r"\ln L(", r"p", r")", r"=", r"(\sum x_i)", r"\ln(p)", r"+", r"(n-\sum x_i)", r"\ln(1-p)",
            font_size=42,
        )
        log_simplified.set_color_by_tex(r"p", YELLOW)
        log_simplified.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                log_wrap,
                log_simplified,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        derivative = MathTex(
            r"\frac{\partial \ln L}{\partial p}", r"=", r"\frac{\sum x_i}{p}", r"-", r"\frac{n-\sum x_i}{1-p}",
            font_size=42,
        )
        derivative.set_color_by_tex(r"p", YELLOW)
        derivative.set_color_by_tex(r"x_i", BLUE)
        brace = SurroundingRectangle(log_simplified, color=GREEN)
        self.play(Create(brace))
        self.play(
            TransformMatchingTex(
                log_simplified,
                derivative,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=3,
            )
        )
        self.play(FadeOut(brace))

        common_denominator = MathTex(
            r"(1-p)\sum x_i - p(n-\sum x_i) = 0",
            font_size=42,
        )
        common_denominator.set_color_by_tex(r"p", YELLOW)
        common_denominator.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                derivative,
                common_denominator,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        p_hat = MathTex(
            r"\hat{p}", r"=", r"\frac{1}{n}\sum x_i", r"=", r"\bar{X}",
            font_size=42,
        )
        p_hat.set_color_by_tex(r"p", YELLOW)
        p_hat.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                common_denominator,
                p_hat,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        second_deriv = MathTex(
            r"\frac{\partial^2 \ln L}{\partial p^2} = -\frac{\sum x_i}{p^2} - \frac{n-\sum x_i}{(1-p)^2} < 0",
            font_size=42,
        )
        second_deriv.set_color_by_tex(r"p", YELLOW)
        second_deriv.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                p_hat.copy(),
                second_deriv,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )
        self.play(FadeOut(second_deriv), FadeOut(p_hat), FadeOut(title))

    def uniform_section(self):
        title = Tex(r"Loi Uniforme $U(0, \theta)$", font_size=48)
        title.set_color_by_tex(r"\theta", YELLOW)
        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP))

        density = MathTex(
            r"f(x) = \frac{1}{\theta} \mathbb{1}_{[0,\theta]}(x)",
            font_size=42,
        )
        density.set_color_by_tex(r"\theta", YELLOW)
        density.set_color_by_tex(r"x", BLUE)
        self.play(Write(density))

        likelihood = MathTex(
            r"L(", r"\theta", r")", r"=", r"\frac{1}{\theta^n}", r"\mathbb{1}_{\max(x_i) \le \theta}",
            font_size=42,
        )
        likelihood.set_color_by_tex(r"\theta", YELLOW)
        likelihood.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                density,
                likelihood,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        constraint = MathTex(
            r"\theta \ge \max(x_i)",
            r"\Rightarrow",
            r"L(\theta) > 0",
            font_size=42,
        )
        constraint.set_color_by_tex(r"\theta", YELLOW)
        constraint.set_color_by_tex(r"x_i", BLUE)
        self.play(
            TransformMatchingTex(
                likelihood,
                constraint,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        monotonic = Tex(
            r"\text{Pour } \theta \text{ minimal } \Rightarrow \theta = \max(X_i)",
            font_size=42,
        )
        monotonic.set_color_by_tex(r"\theta", YELLOW)
        monotonic.set_color_by_tex(r"X", BLUE)
        self.play(
            TransformMatchingTex(
                constraint,
                monotonic,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        reasoning = Tex(
            r"\text{L est max quand } \theta = \max(X_1,\dots,X_n)",
            font_size=42,
        )
        reasoning.set_color_by_tex(r"\theta", YELLOW)
        reasoning.set_color_by_tex(r"X", BLUE)
        self.play(
            TransformMatchingTex(
                monotonic,
                reasoning,
                path_arc=45 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        theta_hat = MathTex(
            r"\hat{\theta}", r"=", r"\max(X_1, \dots, X_n)", r"=", r"X_{(n)}",
            font_size=42,
        )
        theta_hat.set_color_by_tex(r"\theta", YELLOW)
        theta_hat.set_color_by_tex(r"X", BLUE)
        self.play(
            TransformMatchingTex(
                reasoning,
                theta_hat,
                path_arc=90 * DEGREES,
                lag_ratio=0.1,
                run_time=2,
            )
        )
        self.play(FadeOut(theta_hat), FadeOut(title))
